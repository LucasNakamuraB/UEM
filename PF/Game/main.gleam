import gleam/float
import gleam/int
import lib/grid.{
  type Direction, type Grid, type Vector, Down, Grid, Left, Right, Up, Vector,
  g_get, get, get_from_pos, get_from_pos_dir,
}
import sgleam/check
import sgleam/fill
import sgleam/image.{type Image}
import sgleam/key
import sgleam/math
import sgleam/stroke
import sgleam/world

const tile_size: Int = 16

const screen_width: Int = 640

const screen_height: Int = 480

const fov: Float = 90.0

const player_pos = Vectorf(64.0, 64.0)

const player2_pos = Vectorf(64.0, 32.0)

const speed = 2.0

pub type ScreenState {
  ScreenState(position_1: Vectorf, position_2: Vectorf, angle: Int)
}

pub type RayPacket {
  RayPacket(position: Vector, x_side: Bool, number: Int, angle: Float)
}

pub type Vectorf {
  Vectorf(x: Float, y: Float)
}

const map: Grid =
  Grid(
    [
      [2, 1, 1, 99, 99, 1, 2, 2],
      [2, 2, 2, 0, 0, 1, 1, 1],
      [2, 0, 0, 0, 0, 0, 1, 1],
      [2, 0, 0, 0, 0, 0, 0, 1],
      [2, 0, 0, 0, 0, 0, 0, 2],
      [2, 0, 0, 0, 2, 2, 0, 1],
      [1, 0, 2, 0, 0, 2, 0, 1],
      [2, 2, 1, 2, 2, 2, 1, 1],
    ],
  )

pub fn move(pos: Vectorf, angle: Int) {
  let move_angle = int.to_float(angle - 45)
  let new_pos =
    vectorf_sum(
      pos,
      Vectorf(
        speed *. math.sin_deg(move_angle),
        speed *. math.cos_deg(move_angle),
      ),
    )
  case
    map
    |> get_from_pos(
      Vector(float.truncate(new_pos.x), float.truncate(new_pos.y)),
      tile_size,
    )
  {
    0 -> new_pos
    _ -> pos
  }
}

pub fn to_vectori(v: Vectorf) {
  Vector(float.truncate(v.x), float.truncate(v.y))
}

pub fn vectorf_sum(v1: Vectorf, v2: Vectorf) {
  Vectorf({ v1.x +. v2.x }, { v1.y +. v2.y })
}

pub fn vectorf_sub(v1: Vectorf, v2: Vectorf) {
  Vectorf({ v1.x -. v2.x }, { v1.y -. v2.y })
}

// calcula a distância entre dois pontos
pub fn distance(from: Vector, to: Vector) -> Float {
  let x_dist = int.to_float(int.max(from.x, to.x) - int.min(from.x, to.x))
  let y_dist = int.to_float(int.max(from.y, to.y) - int.min(from.y, to.y))
  { math.sqrt({ x_dist *. x_dist } +. { y_dist *. y_dist }) }
}

pub fn tan(angle) -> Float {
  case angle {
    0.0 -> 0.0
    90.0 | 270.0 -> 0.0
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

pub fn between(n: Float, floor: Float, ceiling: Float) -> Bool {
  case { n >=. floor && n <=. ceiling } {
    True -> True
    False -> False
  }
}

// Retorna a direção do cateto adjacente
pub fn get_direction(angle: Float, pos: Vector) -> Direction {
  case { angle |> between(0.0, 45.0) || angle |> between(315.0, 360.0) } {
    True -> Right
    False ->
      case { angle |> between(45.0, 135.0) } {
        True -> Up
        False ->
          case { angle |> between(135.0, 225.0) } {
            True -> Left
            False -> Down
          }
      }
  }
}

// retorna o cateto adjacente com base na direção e posição
pub fn get_adj_side(direction: Direction, pos: Vector) -> Int {
  case direction {
    Up ->
      case pos.y == 0 {
        True -> tile_size
        False -> pos.y
      }
    Down -> tile_size - pos.y
    Left ->
      case pos.x == 0 {
        True -> tile_size
        False -> pos.x
      }
    Right -> tile_size - pos.x
  }
}

// projeta um raycast que nas bordas dos tiles verifica o numero dele na matriz
// do mapa, caso seja diferente de 0, retorna o numero
pub fn raycast_origin(origin: Vector, angle: Float) -> RayPacket {
  let r_pos = Vector(origin.x % tile_size, origin.y % tile_size)
  let dir = get_direction(angle, r_pos)
  case map |> get_from_pos(origin, tile_size) {
    0 -> {
      let adj_side = get_adj_side(dir, r_pos)
      let op_side =
        int.clamp(
          float.truncate(int.to_float(adj_side) *. { tan(angle) }),
          -tile_size,
          tile_size,
        )
      case dir {
        Up -> {
          let op_side =
            int.clamp(
              float.truncate(int.to_float(adj_side) *. { tan(90.0 -. angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            origin,
            Vector(origin.x + { op_side }, origin.y - adj_side),
            angle,
          )
        }
        Down -> {
          let op_side =
            int.clamp(
              float.truncate(int.to_float(adj_side) /. { tan(angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            origin,
            Vector(
              origin.x + { op_side * fsign(math.cos_deg(angle)) },
              origin.y + adj_side,
            ),
            angle,
          )
        }
        Left -> {
          let op_side =
            -1
            * int.clamp(
              float.truncate(int.to_float(adj_side) /. { tan(90.0 -. angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            origin,
            Vector(origin.x - adj_side, origin.y - { op_side }),
            angle,
          )
        }
        Right -> {
          let op_side =
            int.clamp(
              float.truncate(int.to_float(adj_side) /. { tan(angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            origin,
            Vector(
              origin.x + adj_side,
              origin.y - { op_side * fsign(math.sin_deg(angle)) },
            ),
            angle,
          )
        }
      }
    }
    other -> {
      RayPacket(origin, { r_pos.x != 0 }, other, angle)
    }
  }
}

pub fn raycast(init: Vector, origin: Vector, angle: Float) -> RayPacket {
  let r_pos = Vector(origin.x % tile_size, origin.y % tile_size)
  let dir = get_direction(angle, r_pos)
  case map |> get_from_pos_dir(init, origin, tile_size) {
    0 -> {
      let adj_side = get_adj_side(dir, r_pos)
      let op_side =
        int.clamp(
          float.truncate(int.to_float(adj_side) *. { tan(90.0 -. angle) }),
          -tile_size,
          tile_size,
        )

      case dir {
        Up -> {
          echo origin
          let op_side =
            int.clamp(
              float.truncate(int.to_float(adj_side) *. { tan(90.0 -. angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            init,
            Vector(origin.x + { op_side }, origin.y - adj_side),
            angle,
          )
        }
        Down -> {
          let op_side =
            int.clamp(
              float.truncate(int.to_float(adj_side) /. { tan(angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            init,
            Vector(
              origin.x + { op_side * fsign(math.cos_deg(angle)) },
              origin.y + adj_side,
            ),
            angle,
          )
        }
        Left -> {
          let op_side =
            -1
            * int.clamp(
              float.truncate(int.to_float(adj_side) /. { tan(90.0 -. angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            init,
            Vector(origin.x - adj_side, origin.y - { op_side }),
            angle,
          )
        }
        Right -> {
          let op_side =
            int.clamp(
              float.truncate(int.to_float(adj_side) /. { tan(angle) }),
              -tile_size,
              tile_size,
            )
          raycast(
            init,
            Vector(
              origin.x + adj_side,
              origin.y - { op_side * fsign(math.sin_deg(angle)) },
            ),
            angle,
          )
        }
      }
    }
    other -> {
      RayPacket(origin, { r_pos.x > r_pos.y }, other, angle)
      echo RayPacket(origin, { r_pos.x > r_pos.y }, other, angle)
    }
  }
}

pub fn is_x_side(pos: Vectorf, tile_size) {
  let i_pos =
    Vector(float.truncate(pos.x) % tile_size, float.truncate(pos.y) % tile_size)
  case i_pos.x > { tile_size / 2 } {
    True ->
      case i_pos.y > { tile_size / 2 } {
        True -> {
          i_pos.x < i_pos.y
        }
        False -> {
          i_pos.x < { tile_size - i_pos.y }
        }
      }
    False ->
      case i_pos.y > { tile_size / 2 } {
        True -> { tile_size - i_pos.x } < i_pos.y
        False -> { tile_size - i_pos.x } < { tile_size - i_pos.y }
      }
  }
}

pub fn raycast_i(pos: Vectorf, angle: Float, step: Float) -> RayPacket {
  let i_pos = Vector(float.truncate(pos.x), float.truncate(pos.y))
  case
    map
    |> get_from_pos(
      Vector(float.truncate(pos.x), float.truncate(pos.y)),
      tile_size,
    )
  {
    0 -> {
      let x_side = step *. math.cos_deg(angle) *. -1.0
      let y_side = step *. math.sin_deg(angle)
      raycast_i(Vectorf({ pos.x +. x_side }, { pos.y +. y_side }), angle, step)
    }
    other -> RayPacket(i_pos, is_x_side(pos, tile_size), other, angle)
  }
}

// gera uma fita para ser colocada na tela
pub fn generate_strip(origin: Vector, packet: RayPacket) -> image.Image {
  let dist =
    float.truncate(
      distance(origin, packet.position) *. math.sin_deg(packet.angle),
    )
  let height =
    float.truncate(
      { int.to_float(screen_height / int.absolute_value(dist)) } *. 10.0,
    )

  let width = 8

  case packet.number, packet.x_side {
    1, True -> {
      let color = fill.blue
      image.rectangle(width, height, color)
    }
    1, False -> {
      let color = fill.darkblue
      image.rectangle(width, height, color)
    }
    2, True -> {
      let color = fill.red
      image.rectangle(width, height, color)
    }
    2, False -> {
      let color = fill.darkred
      image.rectangle(width, height, color)
    }
    _, _ -> {
      let color = fill.yellow
      image.rectangle(width, height, color)
    }
  }
}

pub fn draw_player(self: Vector, pos: Vector) -> image.Image {
  let dist = float.truncate(distance(self, pos))
  image.star(screen_height / dist, fill.hotpink)
}

pub fn vision_sweep(
  scr: image.Image,
  start: Float,
  angle: Float,
  end_angle: Float,
  pos: Vectorf,
) {
  let i_pos = to_vectori(pos)
  let iangle = float.truncate(angle) % 360
  let step = 2.0
  let pack = raycast_i(pos, angle, step)
  let deltapack =
    RayPacket(
      pack.position,
      pack.x_side,
      pack.number,
      pack.angle -. start +. 45.0,
    )
  case angle == end_angle {
    False ->
      vision_sweep(
        scr
          |> image.place_image(
            screen_width
              - { { screen_width / 90 } * float.truncate(angle -. start) },
            { screen_height / 2 },
            generate_strip(i_pos, deltapack),
          ),
        start,
        angle +. 1.0,
        end_angle,
        pos,
      )
    True ->
      scr
      |> image.place_image(
        screen_width - { { screen_width / 90 } * float.truncate(angle) },
        { screen_height / 2 },
        generate_strip(i_pos, deltapack),
      )
  }
}

pub fn create_screen(state: ScreenState) -> Image {
  //echo raycast(player_pos, Vector(96, 48), 10.0)
  let scr = image.empty_scene(screen_width, screen_height)
  let scr =
    scr
    |> image.place_image(
      screen_width / 2,
      screen_height / 4,
      image.rectangle(screen_width, screen_height / 2, fill.gray),
    )
  let scr =
    scr
    |> image.place_image(
      screen_width / 2,
      { screen_height / 4 } * 3,
      image.rectangle(screen_width, screen_height / 2, fill.darkslategray),
    )
  let scr =
    scr
    |> image.place_image(
      screen_width / 2,
      screen_height / 2,
      draw_player(to_vectori(state.position_1), to_vectori(state.position_2)),
    )
  scr
  |> vision_sweep(
    int.to_float(state.angle),
    int.to_float(state.angle),
    int.to_float(state.angle + 92),
    state.position_1,
  )
}

pub fn turn_camera(state: ScreenState, key: key.Event) {
  case key {
    key.ArrowLeft ->
      ScreenState(state.position_1, state.position_2, state.angle + 5)
    key.ArrowRight ->
      ScreenState(state.position_1, state.position_2, state.angle - 5)
    key.ArrowUp ->
      ScreenState(
        move(state.position_1, state.angle),
        state.position_2,
        state.angle,
      )
    key.ArrowDown ->
      ScreenState(
        move(state.position_1, { state.angle - 180 }),
        state.position_2,
        state.angle,
      )
    _ -> state
  }
}

pub fn main() {
  todo
}

pub fn smain() {
  world.create(ScreenState(player_pos, player2_pos, 0), create_screen)
  |> world.on_key_press(turn_camera)
}

//pub fn raycast_examples() {
//  // direção: Up
//  raycast(Vector(11, 27), 90.0) |> check.eq(1)
//  // direção: Left
//  raycast(Vector(21, 12), 180.0) |> check.eq(2)
//  // direção: Right
//  raycast(Vector(11, 12), 18.0) |> check.eq(3)
//  //direção: Down
//  raycast(Vector(13, 11), 270.0) |> check.eq(1)
//}

pub fn get_direction_examples() {
  get_direction(0.0, Vector(0, 4)) |> check.eq(Right)
  get_direction(180.0, Vector(0, 4)) |> check.eq(Left)
  get_direction(90.0, Vector(4, 0)) |> check.eq(Up)
  get_direction(270.0, Vector(4, 0)) |> check.eq(Down)
}
