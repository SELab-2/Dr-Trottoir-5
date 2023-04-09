import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST,
  FormMultipart,
  FormField, GET, Path
} from "@/api/EchoFetch";
import Building from "@/api/models/Building";
import BuildingManual from "@/api/models/BuildingManual";
import config from "@/config";
import {BuildingManualStatus} from "@/api/models/BuildingManualStatus";
import {InputFields} from "@/types/fields/InputFields";

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
  createBuilding(@Body() body: InputFields): EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }

  /**
   * Get building information
   */
  @GET('/ronde/building/{id}')
  getBuildingById(@Path('id') id : number) : EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(BuildingService);
