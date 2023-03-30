import {Body, Header, EchoPromise, EchoService, EchoServiceBuilder, POST} from "@/api/EchoFetch";
import Building from "@/api/models/Building";
import {InputField} from "@/types/fields/InputField";
import BuildingManual from "@/api/models/BuildingManual";
import config from "@/config";

class BuildingService extends EchoService {
  /**
   * Add building manual
   */
  @POST('/ronde/building/manual/')
  createManual(@Body() body: InputField, @Header('Content-Type') header): EchoPromise<BuildingManual> {
    return {} as EchoPromise<BuildingManual>
  }

  /**
   * Create a new building
   */
  @POST('/ronde/building/')
  createBuilding(@Body() body: InputField) : EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(BuildingService);
