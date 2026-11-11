import gleam/float
import gleam/int
import sgleam/check
import sgleam/math

pub type Direction {
  Up
  Down
  Left
  Right
}

pub type Vector {
  Vector(x: Int, y: Int)
}

pub type Grid {
  Grid(matrix: List(List(Int)))
}

// retorna a distancia entre dois pontos
pub fn dist(a: Vector, b: Vector) -> Int {
  let c = {
    int.max(a.x, b.x) - int.min(a.x, b.x)
  }
  let d = {
    int.max(a.y, b.y) - int.min(a.y, b.y)
  }
  float.truncate(math.sqrt({ int.to_float(c * c) } +. { int.to_float(d * d) }))
}

pub fn dist_examples() {
  dist(Vector(0, 0), Vector(0, 0)) |> check.eq(0)
  dist(Vector(0, 2), Vector(0, 6)) |> check.eq(4)
  dist(Vector(1, 0), Vector(2, 0)) |> check.eq(1)
  dist(Vector(0, 0), Vector(3, 4)) |> check.eq(5)
}

// Retorna o elemento de indice *index* em *lst*
pub fn get(lst: List(Int), index: Int) -> Int {
  case lst, index {
    [], _ -> 0
    [first, ..], 0 -> first
    [_, ..tail], _ -> get(tail, index - 1)
  }
}

// Auxiliar, get com lista de lista
pub fn get_l(lst: List(List(Int)), index: Int) -> List(Int) {
  case lst, index {
    [], _ -> []
    [first, ..], 0 -> first
    [_, ..tail], _ -> get_l(tail, index - 1)
  }
}

// Retorna o elemento de posição (x, y) na matriz de *grid*, sendo x=j e y=i
pub fn g_get(grid: Grid, x: Int, y: Int) -> Int {
  { grid.matrix |> get_l(y) } |> get(x)
}

pub fn get_examples() {
  check.eq(get([0, 1, 2, 3], 2), 2)
  check.eq(get([0, 1, 2, 3], 5), 0)
  check.eq(get([], 2), 0)
}

pub fn g_get_examples() {
  let g = Grid([[1, 2, 3], [6, 4, 0], [9, 8, 1]])
  check.eq(g_get(g, 0, 0), 1)
  check.eq(g_get(g, 2, 0), 3)
  check.eq(g_get(g, 1, 1), 4)
}

pub fn get_from_pos(grid: Grid, pos: Vector, tile_size: Int) -> Int {
  let grid_x = pos.x / tile_size
  let grid_y = pos.y / tile_size
  grid |> g_get(grid_x, grid_y)
}

pub fn get_from_pos_dir(
  grid: Grid,
  origin: Vector,
  pos: Vector,
  tile_size: Int,
) -> Int {
  let grid_x = pos.x / tile_size
  let grid_y = pos.y / tile_size
  case { pos.x % tile_size } == 0 {
    True ->
      case origin.x > pos.x {
        True -> grid |> g_get({ grid_x - 1 }, { grid_y })
        False -> grid |> g_get({ grid_x }, { grid_y })
      }
    False ->
      case origin.y > pos.y {
        True -> grid |> g_get(grid_x, { grid_y })
        False -> grid |> g_get(grid_x, { grid_y })
      }
  }
}

pub fn get_from_pos_examples() {
  let g = Grid([[0, 1, 2], [10, 11, 12], [20, 21, 22]])
  check.eq(get_from_pos(g, Vector(12, 4), 8), 1)
  check.eq(get_from_pos(g, Vector(4, 4), 8), 0)
  check.eq(get_from_pos(g, Vector(8, 20), 8), 21)
}
//pub fn get_from_pos_dir_examples() {
//  let g = Grid([[0, 1, 2], [10, 11, 12], [20, 21, 22]])
//  check.eq(get_from_pos_dir(g, Vector(12, 8), Up, 8), 1)
//  check.eq(get_from_pos_dir(g, Vector(12, 16), Down, 8), 21)
//  check.eq(get_from_pos_dir(g, Vector(8, 12), Left, 8), 10)
//  check.eq(get_from_pos_dir(g, Vector(16, 12), Right, 8), 12)
//}
