import PickupDay from "@/api/models/PickupDay";

export default class Container {
  id: number;
  building: number;
  type: string;
  special_actions: string;
  collection_days: [number];
  collection_days_detail: [PickupDay];
}
