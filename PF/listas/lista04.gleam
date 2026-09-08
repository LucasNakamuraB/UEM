import gleam/io

import gleam/float
import gleam/int
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

pub type Resolution {
  Resolution(width: Int, height: Int)
}

pub fn calc_megapixels(res: Resolution) {
  int.to_float({ res.height * res.width }) /. 1_000_000.0
}

pub type AspectRatio {
  R4x3
  R16x9
  Other
}

pub fn get_ratio(res: Resolution) {
  let res_ratio = int.to_float(res.width) /. int.to_float(res.height)
  case res_ratio == 4.0 /. 3.0 {
    True -> R4x3
    False ->
      case res_ratio == 16.0 /. 9.0 {
        True -> R16x9
        False -> Other
      }
  }
}

pub fn fits(img: Resolution, screen: Resolution) {
  case img.width <= screen.width, img.height <= screen.height {
    True, True -> True
    _, _ -> False
  }
}

pub type Shape {
  Rect(width: Float, height: Float)
  Circle(radius: Float)
}

pub fn area(shape: Shape) {
  case shape {
    Rect(width, height) -> width *. height
    Circle(radius) -> radius *. radius *. 3.14
  }
}

pub fn shape_fits(inner_shape: Shape, outer_shape: Shape) -> Bool {
  case outer_shape {
    Rect(o_width, o_height) ->
      case inner_shape {
        Rect(i_width, i_height) ->
          { i_width <=. o_width } && { i_height <=. o_height }
        Circle(i_radius) ->
          { i_radius *. 2.0 <=. o_width } && { i_radius *. 2.0 <=. o_height }
      }
    Circle(o_radius) ->
      case inner_shape {
        Rect(i_width, i_height) ->
          { { i_width *. i_width } +. { i_height *. i_height } }
          <=. { o_radius *. o_radius *. 4.0 }
        Circle(i_radius) -> {
          i_radius <=. o_radius
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
  // calc_megapixels()
  check.eq(calc_megapixels(Resolution(0, 0)), 0.0)
  check.eq(calc_megapixels(Resolution(1000, 1000)), 1.0)
  check.eq(calc_megapixels(Resolution(1000, 1500)), 1.5)
  check.eq(calc_megapixels(Resolution(2000, 2000)), 4.0)
  // get_ratio()
  check.eq(get_ratio(Resolution(1, 1)), Other)
  check.eq(get_ratio(Resolution(160, 90)), R16x9)
  check.eq(get_ratio(Resolution(800, 600)), R4x3)
  // fits()
  check.eq(fits(Resolution(100, 100), Resolution(100, 100)), True)
  check.eq(fits(Resolution(200, 100), Resolution(100, 100)), False)
  check.eq(fits(Resolution(100, 200), Resolution(100, 100)), False)
  check.eq(fits(Resolution(10, 10), Resolution(100, 100)), True)
  check.eq(fits(Resolution(10, 10), Resolution(100, 100)), True)
  // area()
  check.eq(area(Rect(6.0, 7.0)), 42.0)
  check.eq(area(Circle(10.0)), 314.0)
  // shape_fits()
  check.eq(shape_fits(Rect(1.0, 1.0), Rect(1.0, 1.0)), True)
  check.eq(shape_fits(Rect(2.0, 1.0), Rect(1.0, 1.0)), False)
  check.eq(shape_fits(Rect(1.0, 1.0), Circle(2.0)), True)
  check.eq(shape_fits(Rect(3.0, 1.0), Circle(1.0)), False)
  check.eq(shape_fits(Circle(1.0), Rect(2.0, 2.0)), True)
  check.eq(shape_fits(Circle(3.0), Rect(1.0, 1.0)), False)
  check.eq(shape_fits(Circle(1.0), Rect(3.0, 3.0)), True)
  check.eq(shape_fits(Circle(1.0), Rect(1.0, 1.0)), False)
}
