import {
  Body,
  DELETE,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  PATCH,
  POST,
  Query
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import DayPlanning from "@/api/models/Planning";
import Building from "@/api/models/Building";
import Round from "@/api/models/Round";

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
   * Get a list of all the rows
   */
  @GET("/ronde/")
  getRounds() : EchoPromise<Array<Round>> {
    return {} as EchoPromise<Array<Round>>
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(PlanningService);
