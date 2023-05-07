import {Body, EchoPromise, EchoService, EchoServiceBuilder, GET, PATCH, Path, POST} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import TrashTemplate from "@/api/models/TrashTemplate";
import Container from "@/api/models/Container";
import Building from "@/api/models/Building";
import {TrashTemplateWrapper} from "@/api/wrappers/TrashTemplateWrapper";
import ContainerWrapper from "@/api/wrappers/ContainerWrapper";

class TrashTemplateService extends EchoService {

  /* All the needed GET requests */
  @GET("/trashtemplates/")
  getTrashTemplates(): EchoPromise<TrashTemplate[]> {
    return {} as EchoPromise<TrashTemplate[]>;
  }

  @GET("/trashtemplates/{id}/")
  getTrashTemplate(@Path('id') id: number): EchoPromise<TrashTemplate> {
    return {} as EchoPromise<TrashTemplate>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/")
  getTrashContainersOfTemplate(@Path('id') id: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/eenmalig/")
  getTrashContainersOfTemplateEenmalig(@Path('id') id: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/{extraId}/eenmalig/")
  getTrashContainersEenmaligOfTemplateByExtraId(@Path('id') id: number, @Path('extraId') extraId: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/{extraId}/")
  getTrashContainersOfTemplateByExtraId(@Path('id') id: number, @Path('extraId') extraId: number): EchoPromise<Container> {
    return {} as EchoPromise<Container>;
  }

  @GET("/trashtemplates/{id}/buildings/")
  getBuildingsOfTemplate(@Path('id') id: number): EchoPromise<Building[]> {
    return {} as EchoPromise<Building[]>;
  }

  @GET("/trashtemplates/{id}/buildings/eenmalig/")
  getBuildingsEenmaligOfTemplate(@Path('id') id: number): EchoPromise<Building[]> {
    return {} as EchoPromise<Building[]>;
  }

  @GET("/trashtemplates/{id}/buildings/{buildingId}/")
  getBuildingOfTemplate(@Path('id') id: number, @Path('buildingId') buildingId: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>;
  }

  @GET("/trashtemplates/{id}/buildings/{buildingId}/eenmalig/")
  getBuildingEenmaligOfTemplate(@Path('id') id: number, @Path('buildingId') buildingId: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>;
  }

  /* All the needed POST requests */

  @POST("/trashtemplates/")
  newTrashTemplate(@Body() body: TrashTemplateWrapper): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @POST("/trashtemplates/{id}/trashcontainers/")
  newContainerToTemplate(@Path('id') id: number, @Body() body: ContainerWrapper): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @POST("/trashtemplates/{id}/trashcontainers/eenmalig/")
  newContainerToTemplateEenmalig(@Path('id') id: number, @Body() body: Container): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @POST("/trashtemplates/{id}/buildings/")
  newBuildingToTemplate(@Path('id') id: number, @Body() body: Object): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @POST("/trashtemplates/{id}/buildings/eenmalig/")
  newBuildingToTemplateEenmalig(@Path('id') id: number, @Body() body: Object): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /* All the needed PATCH requests */

  @PATCH("/trashtemplates/{id}/")
  updateTrashTemplate(@Path('id') id: number, @Body() body: TrashTemplateWrapper): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @PATCH("/trashtemplates/{id}/trashcontainers/{containerId}/")
  updateContainerTemplate(@Path('id') id: number, @Path('containerId') containerId: number, @Body() body: ContainerWrapper): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @PATCH("/trashtemplates/{id}/trashcontainers/{containerId}/eenmalig/")
  updateContainerTemplateEenmalig(@Path('id') id: number, @Path('containerId') containerId: number, @Body() body: Container): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @PATCH("/trashtemplates/{id}/buildings/")
  updateBuildingTemplate(@Path('id') id: number, @Body() body: Object): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @PATCH("/trashtemplates/{id}/buildings/eenmalig/")
  updateBuildingTemplateEenmalig(@Path('id') id: number, @Body() body: Object): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(TrashTemplateService);
