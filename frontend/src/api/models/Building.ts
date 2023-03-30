import BuildingManual from "@/api/models/BuildingManual";

export default class Building{
  id: number;
  adres: String;
  ivago_klantr: number;
  manual: BuildingManual;
  containers: null; // TODO Add model
  location: null; // TODO Add model
  buildingID: number; // Maybe add UUID Type?
}
