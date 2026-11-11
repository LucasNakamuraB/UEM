import gleam/float
import gleam/int
import lib/grid.{
  type Direction, type Grid, type Vector, Down, Grid, Left, Right, Up, Vector,
  g_get, get, get_from_pos, get_from_pos_dir,
}
import sgleam/check
import sgleam/math

const tile_size = 8

const map: Grid =
  Grid(
    [
      [4, 1, 3, 3, 3, 1, 1, 1],
      [2, 0, 0, 0, 0, 0, 0, 1],
      [5, 0, 0, 0, 1, 0, 0, 1],
      [2, 0, 0, 1, 1, 1, 0, 1],
      [2, 0, 0, 0, 1, 0, 0, 1],
      [2, 0, 0, 0, 0, 0, 0, 1],
      [2, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
    ],
  )

pub fn tan(angle) -> Float {
  case angle {
    0.0 -> 0.0
    90.0 -> 1000.0
    _ -> {
      math.sin_deg(angle) /. math.cos_deg(angle)
    }
  }
}

pub fn fsign(x: Float) -> Int {
  case x >=. 0.0 {
    True -> 1
    False -> -1
  }
}

// Retorna a direção do cateto adjacente
pub fn get_direction(angle: Float, pos: Vector) -> Direction {
  case pos.x < pos.y {
    True ->
      case math.cos_deg(angle) >. 0.0 {
        True -> Right
        False -> Left
      }
    False ->
      case math.sin_deg(angle) >. 0.0 {
        True -> Up
        False -> Down
      }
  }
}

// retorna o cateto adjacente com base na direção e posição
pub fn get_adj_side(direction: Direction, pos: Vector) -> Int {
  case direction {
    Up -> tile_size - pos.x
    Down -> pos.x
    Left -> pos.x
    Right -> tile_size - pos.x
  }
}

// projeta um raycast que nas bordas dos tiles verifica o numero dele na matriz
// do mapa, caso seja diferente de 0, retorna o numero
pub fn raycast(origin: Vector, angle: Float) -> Int {
  let r_pos = Vector(origin.x % tile_size, origin.y % tile_size)
  let dir = get_direction(angle, r_pos)
  echo angle
  echo dir
  echo origin
  case map |> get_from_pos_dir(origin, dir, tile_size) {
    0 -> {
      let adj_side = get_adj_side(dir, r_pos)
      echo adj_side
      let op_side =
        int.clamp(
          float.truncate(int.to_float(adj_side) *. { tan(angle) }),
          0,
          tile_size,
        )
      case dir {
        Up ->
          raycast(
            Vector(
              origin.x + { op_side * fsign(math.cos_deg(angle)) },
              origin.y - adj_side,
            ),
            angle,
          )
        Down ->
          raycast(
            Vector(
              origin.x + { op_side * fsign(math.cos_deg(angle)) },
              origin.y + adj_side,
            ),
            angle,
          )
        Left ->
          raycast(
            Vector(
              origin.x - adj_side,
              origin.y - { op_side * fsign(math.sin_deg(angle)) },
            ),
            angle,
          )
        Right ->
          raycast(
            Vector(
              origin.x + adj_side,
              [
              origin.y - { op_side * fsign(math.sin_deg(angle)) },
            ),
            angle,
          )
      }
    }
    other -> other
  }
}

pub fn main() {
  todo
}

pub fn raycast_examples() {
  // direção: Up
  raycast(Vector(11, 28), 90.0) |> check.eq(1)
  // direção: Left
  raycast(Vector(11, 12), 180.0) |> check.eq(2)
  // direção: Right
  raycast(Vector(11, 12), 18.0) |> check.eq(3)
  //direção: Down
  raycast(Vector(13, 12), 270.0) |> check.eq(1)
}

pub fn get_direction_examples() {
  get_direction(45.0, Vector(0, 4)) |> check.eq(Right)
  get_direction(120.0, Vector(0, 4)) |> check.eq(Left)
  get_direction(45.0, Vector(4, 0)) |> check.eq(Up)
  get_direction(270.0, Vector(4, 0)) |> check.eq(Down)
}
