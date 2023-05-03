import {mount} from '@vue/test-utils'
import CreateEditMailTemplate from '@/components/admin/mail/CreateEditMailTemplate.vue'
import MailTemplateService from "@/api/services/MailTemplateService";

describe('CreateEditMailTemplate.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateEditMailTemplate);
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

/*it('creates a template when the create button is clicked', async () => {
  // In your test file, create a mock implementation of the MailTemplateService
  const mockMailTemplateService = {
    createMailTemplate: jest.fn().mockResolvedValue(),
  };

  // Replace the original implementation of the MailTemplateService with the mock implementation
  jest.mock("@/api/services/MailTemplateService", () => {
    return jest.fn().mockImplementation(() => {
      return mockMailTemplateService;
    });
  });

  const createButton = wrapper.find('[data-test="create-button"]');
  const name = 'Test template';
  const text = 'Test template text';
  wrapper.vm.template.name = name;
  wrapper.vm.template.text = text;
  createButton.trigger('click');
  await wrapper.vm.$nextTick();

  console.log(mockMailTemplateService.createMailTemplate)

  // Assert that createMailTemplate was called with the correct parameters
  /*expect(mockMailTemplateService.createMailTemplate).toHaveBeenCalledWith({
    name,
    content: text,
  });*/
//});



})
