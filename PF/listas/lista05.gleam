import gleam/int
import gleam/option.{type Option, None, Some}
import sgleam/check

pub type Spectator {
  Child
  Youngster(Option(Int))
  Adult
  Elderly
}

pub fn get_student_id(spec: Spectator) -> Result(Int, Nil) {
  case spec {
    Youngster(id) ->
      case id {
        Some(n) -> Ok(n)
        None -> Error(Nil)
      }
    _ -> Error(Nil)
  }
}

pub fn get_student_id_examples() {
  let yng = Youngster(None)
  let yng_std = Youngster(Some(123))
  check.eq(get_student_id(yng_std), Ok(123))
  check.eq(get_student_id(yng), Error(Nil))
}

pub fn has_discount(spec: Spectator) -> Bool {
  case spec {
    Child | Elderly -> True
    Adult -> False
    Youngster(id) ->
      case id {
        Some(_) -> True
        None -> False
      }
  }
}

pub fn has_discount_examples() {
  check.eq(has_discount(Child), True)
  check.eq(has_discount(Elderly), True)
  check.eq(has_discount(Adult), False)
  check.eq(has_discount(Youngster(Some(234))), True)
  check.eq(has_discount(Youngster(None)), False)
}

pub fn sum_option(num_1: Option(Int), num_2: Option(Int)) -> Option(Int) {
  case num_1, num_2 {
    Some(n1), Some(n2) -> Some(n1 + n2)
    _, _ -> None
  }
}

pub fn sum_option_examples() {
  check.eq(sum_option(Some(1), Some(2)), Some(3))
  check.eq(sum_option(None, Some(2)), None)
  check.eq(sum_option(Some(1), None), None)
  check.eq(sum_option(None, None), None)
}

pub type NumberError {
  NotNumber
  OutOfBounds
}

pub fn month_days(month: String) -> Result(Int, NumberError) {
  case int.parse(month) {
    Ok(n) ->
      case n {
        1 | 3 | 5 | 7 | 8 | 10 | 12 -> Ok(31)
        4 | 6 | 9 | 11 -> Ok(30)
        2 -> Ok(28)
        _ -> Error(OutOfBounds)
      }
    Error(Nil) -> Error(NotNumber)
  }
}

pub fn month_days_examples() {
  check.eq(month_days("7"), Ok(31))
  check.eq(month_days("4"), Ok(30))
  check.eq(month_days("2"), Ok(28))
  check.eq(month_days("24"), Error(OutOfBounds))
  check.eq(month_days("month"), Error(NotNumber))
}



