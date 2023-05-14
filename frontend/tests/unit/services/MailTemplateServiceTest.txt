import nock from "nock";
import MailTemplateService from "@/api/services/MailTemplateService";
import MailTemplate from "@/api/models/MailTemplate";
import {EchoPromise, EchoService, EchoServiceBuilder, POST} from "@/api/EchoFetch";

const MOCK_SERVER_URL = "http://localhost:8000/api";

class TestService extends EchoService {
    @POST("/mailtemplates")
    public post(): EchoPromise<MailTemplate> {
        return <EchoPromise<MailTemplate>>{}
    };
}

function setupService(): TestService {
    return new EchoServiceBuilder()
        .setBaseUrl(MOCK_SERVER_URL)
        .build(TestService);
}

describe('MailTemplateService', () => {
  afterEach(() => {
    nock.cleanAll();
  });

  it('createMailTemplate', async () => {
    const expectedResponse = new MailTemplate();
    expectedResponse.id = 1;
    expectedResponse.name = 'test-template';
    expectedResponse.content = 'test';

    const scope = nock(MOCK_SERVER_URL)
      .post('/mailtemplates')
      .reply(200, expectedResponse);

    const service = setupService();
    const response = await service.post();

    expect(response).toEqual(expectedResponse);
    expect(scope.isDone()).toBeTruthy();
  });

});
