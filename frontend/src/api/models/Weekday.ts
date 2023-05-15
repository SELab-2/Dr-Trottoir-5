export enum Weekday {
  Maandag,
  Dinsdag,
  Woensdag,
  Donderdag,
  Vrijdag,
  Zaterdag,
  Zondag
}

export function weekday_to_api(type: string): String {
  if (type === 'Maandag' ){
    return "MO"
  } else if (type === 'Dinsdag') {
    return "TU"
  } else if (type ===  'Woensdag') {
    return "WE"
  } else if (type === 'Donderdag') {
    return "TH"
  } else if (type === 'Vrijdag') {
    return "FR"
  } else if (type === 'Zaterdag') {
    return "SA"
  } else if (type === 'Zondag') {
    return "SU"
  }
}

export function weekday_from_api(type: String): Weekday {
  if (type === "MO"){
    return Weekday.Maandag
  } else if (type === "TU") {
    return Weekday.Dinsdag
  } else if (type === "WE") {
    return Weekday.Woensdag
  } else if (type === "TH") {
    return Weekday.Donderdag
  } else if (type === "FR") {
    return Weekday.Vrijdag
  } else if (type === "SA") {
    return Weekday.Zaterdag
  } else if (type === "SU") {
    return Weekday.Zondag
  }
}

