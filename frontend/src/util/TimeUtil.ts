export function toTimeString (time) {
  const hours = Math.floor(time / 60)
  let strHours = hours.toString()
  if (hours < 10) { strHours = '0' + strHours }
  const min = time % 60
  let strMin = min.toString()
  if (min < 10) { strMin = '0' + strMin }
  return strHours + ':' + strMin
}
