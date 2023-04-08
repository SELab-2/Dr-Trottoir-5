import BuildingManual from "@/api/models/BuildingManual";

export default class Building{
  id: number;
  adres: string;
  ivago_klantnr: number;
  buildingID: string;
  manual: BuildingManual;
  containers: null; // TODO Add model
  location: null; // TODO Add model
}
