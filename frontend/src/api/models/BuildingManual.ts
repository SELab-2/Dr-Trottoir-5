import { BuildingManualStatus } from '@/api/models/BuildingManualStatus'

export default class BuildingManual {
  id: number;
  file: File;
  fileType: string;
  manualStatus: BuildingManualStatus
}
