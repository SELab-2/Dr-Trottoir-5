import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST,
  FormMultipart,
  FormField
} from "@/api/EchoFetch";
import Building from "@/api/models/Building";
import {InputField} from "@/types/fields/InputField";
import BuildingManual from "@/api/models/BuildingManual";
import config from "@/config";
import {BuildingManualStatus} from "@/api/models/BuildingManualStatus";

class BuildingService extends EchoService {
  /**
   * Add building manual
   */
  @FormMultipart()
  @POST('/ronde/building/manual/')
  createManual(@FormField('file') file : File,
               @FormField('fileType') fileType : string,
               @FormField('manualStatus') manualStatus : BuildingManualStatus): EchoPromise<BuildingManual> {
    return {} as EchoPromise<BuildingManual>
  }

  /**
   * Create a new building
   */
  @POST('/ronde/building/')
  createBuilding(@Body() body: InputField): EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(BuildingService);
