import {mount} from '@vue/test-utils'
import CreateEditMailTemplate from '@/components/admin/mail/CreateEditMailTemplate.vue'
import MailTemplateService from "@/api/services/MailTemplateService";
import {RequestHandler} from "@/api/RequestHandler";

jest.mock('@/api/services/MailTemplateService');
jest.mock("@/api/RequestHandler");
describe('CreateEditMailTemplate.vue', () => {

  let wrapper;


  beforeEach(() => {
    wrapper = mount(CreateEditMailTemplate);
  });

  afterEach(() => {
    jest.clearAllMocks()
  })


  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('Render title create', () => {
    expect(wrapper.find('h1').text()).toMatch('Mail template aanmaken')
  })

  it('Render title edit', async () => {
    wrapper.setProps({edit: true})
    await wrapper.vm.$nextTick()
    expect(wrapper.find('h1').text()).toMatch('Mail template aanpassen')
  })

  it('sets the v-model of v-text-field for the name of the mail template', () => {
    const textField = wrapper.find('v-text-field')
    textField.element.value = 'test';
    textField.trigger('input');
    expect(wrapper.vm.$data.template.name).toBe('test');
  })

  it('sets the v-model of v-textarea for the text of the mail template', () => {
    const textArea = wrapper.find('v-textarea')
    textArea.element.value = 'Dit is een test mail template #test#';
    textArea.trigger('input');
    expect(wrapper.vm.$data.template.text).toBe('Dit is een test mail template #test#');
  })

  it('opens the dialog when the information icon is clicked', async () => {
    const infoIcon = wrapper.find('v-icon');
    infoIcon.trigger('click');
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.showDialog).toBe(true);
  });


  it('calls createMailTemplate with the correct parameters', async () => {
    const wrapper = mount(CreateEditMailTemplate, {
      propsData: {
        edit: false
      }
    })

    wrapper.setData({
      template: {
        name: 'Test template',
        text: 'Hello #name#, this is a test email for #purpose#.'
      }
    })
    RequestHandler.handle.mockResolvedValue(Promise.resolve());

    const createButton = wrapper.find('[data-test="create-button"]');
    await wrapper.vm.$nextTick();
    createButton.trigger('click');

    expect(MailTemplateService.createMailTemplate).toHaveBeenCalledWith({
      name: 'Test template',
      content: 'Hello #name#, this is a test email for #purpose#.'
    })
  })


})
