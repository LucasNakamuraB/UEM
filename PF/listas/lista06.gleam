import gleam/int
import gleam/io
import sgleam/check

pub fn concatena_lista(lst: List(String)) -> String {
  case lst {
    [] -> ""
    [primeiro, ..resto] -> primeiro <> concatena_lista(resto)
  }
}

pub fn concatena_lista_examples() {
  check.eq(concatena_lista(["a", "b", "c"]), "abc")
  check.eq(concatena_lista([]), "")
  check.eq(concatena_lista(["67"]), "67")
}

pub fn size(lst: List(Int)) -> Int {
  case lst {
    [] -> 0
    [_x] -> 1
    [_first, ..rest] -> 1 + size(rest)
  }
}

pub fn size_examples() {
  check.eq(size([]), 0)
  check.eq(size([1]), 1)
  check.eq(size([1, 2, 3, 4]), 4)
}

pub fn to_string_list(lst: List(Int)) -> List(String) {
  case lst {
    [] -> []
    [x] -> [int.to_string(x)]
    [first, ..rest] -> [int.to_string(first), ..to_string_list(rest)]
  }
}

pub fn to_string_list_examples() {
  check.eq(to_string_list([]), [])
  check.eq(to_string_list([69]), ["69"])
  check.eq(to_string_list([2, 3, 4, 1]), ["2", "3", "4", "1"])
}

pub fn remove_empty_str(lst: List(String)) -> List(String) {
  case lst {
    [] -> []
    [str] ->
      case str {
        "" -> []
        _ -> [str]
      }
    ["", ..rest] -> remove_empty_str(rest)
    [first, ..rest] -> [first, ..remove_empty_str(rest)]
  }
}

pub fn remove_empty_str_examples() {
  check.eq(remove_empty_str([]), [])
  check.eq(remove_empty_str(["abc"]), ["abc"])
  check.eq(remove_empty_str([""]), [])
  check.eq(remove_empty_str(["six", "", "seven", ""]), ["six", "seven"])
  check.eq(remove_empty_str(["a", "b", "c", "d"]), ["a", "b", "c", "d"])
}

pub fn all_true(lst: List(Bool)) -> Bool {
  lst == []
  || {
    let assert [first, ..rest] = lst
    first && { all_true(rest) }
  }
}

pub fn all_true_examples() {
  check.eq(all_true([]), True)
  check.eq(all_true([True, True, False]), False)
  check.eq(all_true([True, True, True]), True)
  check.eq(all_true([True, True, True, False, True]), False)
  check.eq(all_true([True, True, True, True, True]), True)

  check.eq(all_true([True]), True)
  check.eq(all_true([False]), False)
}
