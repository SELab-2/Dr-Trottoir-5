import {ContainerType} from "@/api/models/ContainerType";

export enum Weekday {
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  SUNDAY
}

export function weekday_to_api(type: Weekday): String {
  return type.toString().substring(0,2)
}

export function weekday_from_api(type: String): Weekday {
  if (type === "MO"){
    return Weekday.MONDAY
  } else if (type === "TU") {
    return Weekday.TUESDAY
  } else if (type === "WE") {
    return Weekday.WEDNESDAY
  } else if (type === "TH") {
    return Weekday.THURSDAY
  } else if (type === "FR") {
    return Weekday.FRIDAY
  } else if (type === "SA") {
    return Weekday.SATURDAY
  } else if (type === "SU") {
    return Weekday.SUNDAY
  }
}

