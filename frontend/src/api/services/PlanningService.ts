import {
  DELETE,
  EchoPromise,
  EchoService,
  EchoServiceBuilder, FormField, FormMultipart,
  GET, Path, POST,
  Query
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import DayPlanning from "@/api/models/Planning";
import BuildingInfo from "@/api/models/BuildingInfo";

class PlanningService extends EchoService {
  /**
   * Get a day planning.
   */
  @GET("/planning/dagplanning/")
  get(@Query('student') student: string,
      @Query('date') date: string): EchoPromise<DayPlanning> {
    return {} as EchoPromise<DayPlanning>;
  }

  /**
   * Get building info for a day planning
   */
  @GET("/planning/infoperbuilding/")
  getInfo(@Query('dagPlanning') dagPlanning: number): EchoPromise<BuildingInfo> {
    return {} as EchoPromise<BuildingInfo>;
  }

  /**
   * Get student images for building info
   */
  @GET("/planning/buildingpicture/")
  getPictures(@Query('infoPerBuilding') infoPerBuilding: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Delete a building picture
   */
  @DELETE("/planning/buildingpicture/{id}/")
  deletePicture(@Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Post building picture
   */
  @POST("/planning/buildingpicture/")
  @FormMultipart()
  uploadPicture(
    @FormField("image") image: File,
    @FormField("infoPerBuilding") infoPerBuilding: number,
    @FormField("pictureType") pictureType: string,
    @FormField("time") time: string,
    @FormField("remark") remark: string
  ): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(PlanningService);
