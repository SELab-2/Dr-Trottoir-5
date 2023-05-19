import BuildingManual from "@/api/models/BuildingManual";

// TODO fix, object not correct with what backend sends
export default class Building {
  name: string;
  id: number;
  adres: string;
  ivago_klantnr: number;
  buildingID: string;
  manual: BuildingManual;
  containers: null; // TODO Add model
  location: null; // TODO Add model
}
