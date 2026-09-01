import gleam/string
import sgleam/check

pub type Direcao {
  Norte
  Sul
  Leste
  Oeste
}

pub fn dir_oposta(dir: Direcao) {
  case dir {
    Norte -> Sul
    Sul -> Norte
    Leste -> Oeste
    Oeste -> Leste
  }
}

//??????

pub fn noventa_graus_h(dir: Direcao) {
  case dir {
    Norte -> Leste
    Sul -> Oeste
    Leste -> Sul
    Oeste -> Norte
  }
}

pub fn noventa_graus_h_examples() {
  check.eq(noventa_graus_h(Leste), Sul)
}

pub fn noventa_graus_a(dir: Direcao) {
  noventa_graus_h(noventa_graus_h(noventa_graus_h(dir)))
}

pub fn get_angle_h(from: Direcao, to: Direcao) {
  case from == to {
    True -> 0
    False ->
      case noventa_graus_h(from) == to {
        True -> 90
        False ->
          case noventa_graus_a(from) == to {
            True -> 270
            False -> 180
          }
      }
  }
}

pub type Elevador {
  Subindo
  Descendo
  Parado
}

pub fn mover_elevador(from: Int, to: Int) -> Elevador {
  case from == to {
    True -> Parado
    False ->
      case from > to {
        True -> Descendo
        False -> Subindo
      }
  }
}

pub fn elevador_pode_estado(
  estado_elevador: Elevador,
  novo_estado: Elevador,
) -> Bool {
  case estado_elevador, novo_estado {
    Parado, _ -> True
    _, Parado -> True
    _, _ -> False
  }
}

pub type Alinhamento {
  Esquerda
  Direita
  Centro
}

fn ajusta_string(
  s: String,
  num_chars: Int,
  alinhamento: Alinhamento,
) -> String {
  case string.length(s) == num_chars {
    True -> s
    False ->
      case string.length(s) > num_chars {
        True -> string.slice(s, 0, num_chars - 3) <> "..."
        False -> {
          let num_espacos = num_chars - string.length(s)
          case alinhamento {
            Direita -> string.repeat(" ", num_espacos) <> s
            Esquerda -> s <> string.repeat(" ", num_espacos)
            Centro -> {
              let num_espacos_inicio = num_espacos / 2
              let num_espacos_fim = num_espacos - num_espacos_inicio
              string.repeat(" ", num_espacos_inicio)
              <> s
              <> string.repeat(" ", num_espacos_fim)
            }
          }
        }
      }
  }
}

pub fn all_examples() {
  // mover_elevador()
  check.eq(mover_elevador(1, 1), Parado)
  check.eq(mover_elevador(1, 2), Subindo)
  check.eq(mover_elevador(1, 0), Descendo)
  // elevador_pode_estado()
  check.eq(elevador_pode_estado(Parado, Parado), True)
  check.eq(elevador_pode_estado(Subindo, Parado), True)
  check.eq(elevador_pode_estado(Descendo, Parado), True)
  check.eq(elevador_pode_estado(Parado, Subindo), True)
  check.eq(elevador_pode_estado(Parado, Parado), True)
  check.eq(elevador_pode_estado(Parado, Parado), True)
  check.eq(elevador_pode_estado(Subindo, Descendo), False)
  check.eq(elevador_pode_estado(Descendo, Subindo), False)
  // ajusta_string()
  check.eq(ajusta_string("casa", 4, Direita), "casa")
  check.eq(ajusta_string("casa", 4, Esquerda), "casa")
  check.eq(ajusta_string("casa", 4, Centro), "casa")
  check.eq(ajusta_string("casa verde", 7, Direita), "casa...")
  check.eq(ajusta_string("casa verde", 7, Esquerda), "casa...")
  check.eq(ajusta_string("casa verde", 7, Centro), "casa...")
  check.eq(ajusta_string("casa verde", 9, Direita), "casa v...")
  check.eq(ajusta_string("casa", 9, Direita), "     casa")
  check.eq(ajusta_string("casa", 9, Esquerda), "casa     ")
  check.eq(ajusta_string("casa", 9, Centro), "  casa   ")
  check.eq(ajusta_string("casa", 10, Centro), "   casa   ")
}
