export enum ContainerType {
  PMD ,
  REST ,
  PK,
  GLAS,
  GFT
}

export function container_to_api(type: ContainerType): String {
  return type.toString().substring(0,2)
}

export function container_from_api(type: String): ContainerType {
  if (type === "PM"){
    return ContainerType.PMD
  } else if (type === "RE") {
    return ContainerType.REST
  } else if (type === "PK") {
    return ContainerType.PK
  } else if (type === "GL") {
    return ContainerType.GLAS
  } else {
    return ContainerType.GFT
  }
}
