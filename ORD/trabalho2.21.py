from __future__ import annotations
import _struct
import random
import os

ORDEM : int = 4

FORMATO_IDX = "ii"
FORMATO_REF = "i"
TAM_REF = _struct.calcsize(FORMATO_REF)
TAM_IDX = _struct.calcsize(FORMATO_IDX)
TAM_PAG = (TAM_IDX * (ORDEM - 1)) + (TAM_REF * ORDEM)

btree = open("btree.dat", "wb+")

class Chave:
    id: int
    byte_offset: int

    def __init__(self, id, byte_offset):
        self.id = id
        self.byte_offset = byte_offset


class Pagina:

    pai:Pagina
    rrn : int
    chaves: list[Chave]
    refs: list[int]

    def __init__(self):
        self.chaves = []
        self.refs = []
        self.pai = None
        self.rrn = -1

    def is_raiz(self) -> bool:
        return self.pai is None

    def is_folha(self):
        return self.refs == []
    
    def search(self, id: int):
        i = 0
        encontrado = False
        b_off = -2
        while i < len(self.chaves) and not encontrado:
            if id == self.chaves[i].id:
                b_off = self.chaves[i].byte_offset
                encontrado = True
            if id < self.chaves[i].id:
                if self.is_folha():
                    b_off -1
                else:
                    b_off = self.refs[i].search(id)
                encontrado = True
            i += 1
            if not encontrado:
                if self.is_folha():
                        b_off = -1
                else:
                    b_off = self.refs[-1].search(id)
        return b_off
    
    def insert_chave(self, chave: Chave) -> None:
        inserido = False
        i = 0 
        while i < len(self.chaves) and not inserido:
            if chave.id == self.chaves[i].id:
                return
            if chave.id < self.chaves[i].id:
                if self.is_folha():
                    self.chaves = add_to_index(self.chaves, chave, i)
                else:
                   self.refs[i].insert_chave(chave)
                inserido = True
            i += 1
        if not inserido:
            if self.is_folha():
                    self.chaves.append(chave)
            else:
                self.refs[-1].insert_chave(chave)
        write_pagina(self)
        if len(self.chaves) == ORDEM:
            self._split_folha()

    def _split_folha(self):
        new_pag = Pagina()
        new_pag.chaves = self.chaves[ORDEM//2:]
        self.chaves = self.chaves[:ORDEM//2]
        if not self.is_folha:
            new_pag.refs = self.refs[(ORDEM//2) + 1:]
            self.refs = self.refs[(ORDEM//2) + 1:]
        prom = new_pag.chaves.pop(0)

        write_pagina(new_pag)
        if not self.is_raiz():
            self.pai.insert_promo(prom, new_pag)
            print("splitted and promoted")
        else:
            copy = Pagina()
            copy.chaves = self.chaves
            copy.refs = self.refs
            new_raiz = Pagina()
            self.chaves = [prom]
            self.refs = [copy, new_pag]
            write_pagina(copy)
            print("splitted and new root")
        write_pagina(self)



    def insert_promo(self, chave: Chave, filho: Pagina):
        inserido = False
        i = 0 
        while i < len(self.chaves) and not inserido:
            if chave.id < self.chaves[i].id:
                self.chaves = add_to_index(self.chaves, chave, i)
            inserido = True
            i += 1
        if not inserido:
            self.chaves.append(chave)
        self.refs = add_to_index(self.refs, filho, i)
        write_pagina(self)
        if len(self.chaves) == ORDEM:
            self.split_folha()

    def lista_ids(self):
        ids = []
        for chave in self.chaves:
            ids.append(chave.id)
        return ids
    
    def lista_refs(self):
        ids = []
        for chave in self.refs:
            ids.append(chave.rrn)
        return ids

def write_pagina(pagina: Pagina) -> int:
    if pagina.rrn != -1:
        btree.seek(pagina.rrn, os.SEEK_SET)
    else:
        pagina.rrn = btree.seek(0, os.SEEK_END)
    for i in range(ORDEM-1):
        if i < len(pagina.chaves):
            btree.write(_struct.pack(FORMATO_IDX, pagina.chaves[i].id, pagina.chaves[i].byte_offset))
        else:
            btree.write(_struct.pack(FORMATO_IDX, -1, -1))
    for r in range(ORDEM):
        if r < len(pagina.refs):
            btree.write(_struct.pack(FORMATO_REF, pagina.refs[r].rrn))
        else:
            btree.write(_struct.pack(FORMATO_REF, -1))
    return btree.seek(0, os.SEEK_CUR)

def read_pagina(rrn: int) -> Pagina:
    pag: Pagina = Pagina()
    btree.seek(rrn, os.SEEK_SET)
    for i in range(ORDEM - 1):
        buffer = btree.read(TAM_IDX)
        chv_tup = _struct.unpack(FORMATO_IDX, buffer)
        if chv_tup[0] != -1:
            chv = Chave(chv_tup[0], chv_tup[1])
            pag.chaves.append(chv)
    for r in range(ORDEM):
        buffer = btree.read(TAM_REF)
        ref_tup = _struct.unpack(FORMATO_REF, buffer)
        if ref_tup[0] != -1:
            pag.refs.append(ref_tup[0])
    
    pag.rrn = btree.seek(0, os.SEEK_CUR) - TAM_PAG
    return pag

def add_to_index(lst: list, item, idx: int) -> list:
    '''insere atras do indice *idx*'''
    lst = lst[:idx] + [item] + lst[idx:]
    return lst

def imprime_arvore(arvs: list[Pagina]):
    arv_str = ''
    next = []
    refs = []#DEBUG
    for a in arvs:
        refs = refs + a.lista_refs()#DEBUG
        arv_str = arv_str + str(a.lista_ids() )+"("+ str(a.rrn)+ ")"
        for r in a.refs:
            next.append(r)
    print(arv_str)
    #print(refs)
    if arvs == []:
        return
    else:
        imprime_arvore(next)

def imprime_arvore_rrn(arvs: list[Pagina]):
    arv_str = ''
    next = []
    refs = []#DEBUG
    #print(arvs)
    for a in arvs:
        pag = read_pagina(a)
        refs = refs + pag.refs #DEBUG
        arv_str = arv_str + str(pag.lista_ids())
        for r in pag.refs:
            next.append(r)
    print(arv_str)
    #print(refs)
    if arvs == []:
        return
    else:
        imprime_arvore_rrn(next)

def rrn_search(rrn: int, id: int):
    pag = read_pagina(rrn)
    i = 0
    encontrado = False
    b_off = -2
    while i < len(pag.chaves) and not encontrado:
        if id == pag.chaves[i].id:
            b_off = pag.chaves[i].byte_offset
            encontrado = True
        if id < pag.chaves[i].id:
            if pag.is_folha():
                b_off -1                
            else:
                b_off = rrn_search(pag.refs[i], id)
            encontrado = True
        i += 1
        if not encontrado:
            if pag.is_folha():
                b_off = -1
            else:
                b_off = rrn_search(pag.refs[-1], id)
        return b_off

def rrn_insert_chave(pag_rrn, chave: Chave) -> None:
    inserido = False
    i = 0 
    pag = read_pagina(pag_rrn)
    while i < len(pag.chaves) and not inserido:
        if chave.id == pag.chaves[i].id:
            return
        if chave.id < pag.chaves[i].id:
            if pag.is_folha():
                pag.chaves = add_to_index(pag.chaves, chave, i)
            else:
               pag.refs[i].insert_chave(chave)
            inserido = True
        i += 1
    if not inserido:
        if pag.is_folha():
                pag.chaves.append(chave)
        else:
            pag.refs[-1].insert_chave(chave)
    write_pagina(pag)
    if len(pag.chaves) == ORDEM:    
        pag._split_folha()
pag
def rrn_insert_promo(pai_rrn: int, chave: Chave, filho_rrn: int):
    inserido = False
    i = 0 
    pai = read_pagina(pai_rrn)
    filho = read_pagina(filho_rrn)
    while i < len(pai.chaves) and not inserido:
        if chave.id < pai.chaves[i].id:
            pai.chaves = add_to_index(pai.chaves, chave, i)
        inserido = True
        i += 1
    if not inserido:
        pai.chaves.append(chave)
    pai.refs = add_to_index(pai.refs, filho, i)
    write_pagina(pai)
    if len(pai.chaves) == ORDEM:
        pai.split_folha()

def main():
    a = Pagina()
    #a.rrn = 0
    ii = 0
    while ii <= 25:
        intt = random.randint(0, 50)
        a.insert_chave(Chave(intt, intt))
        ii += 1
    print(a.rrn)
    #imprime_arvore([a])
    imprime_arvore_rrn([a.rrn])
    #print(a.search(24))
    print(rrn_search(a.rrn, 24))
    b = read_pagina(a.rrn)
    print(b.lista_ids())

main()
        

