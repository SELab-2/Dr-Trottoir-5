import {mount} from '@vue/test-utils'
import CreateEditMailTemplate from '@/components/admin/mail/CreateEditMailTemplate.vue'

/**
 * Gaat het v-model van een input veld triggeren (omdat de gewone manier niet werkt hebben
 * we deze functie gemaakt)
 */
function triggerInput(input, model, activator) {
  const data = activator(input.element.value)
  model.setData(data)
}


describe('CreateEditMailTemplate.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateEditMailTemplate)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('Render title create', () => {
    expect(wrapper.find('h1').text()).toMatch('Mail template aanmaken')
  })

  it('Render title edit', async () => {
    await wrapper.setProps({edit: true})
    await wrapper.vm.$nextTick()
    expect(wrapper.find('h1').text()).toMatch('Mail template aanpassen')
  })

  it('sets the v-model of v-text-field for the name of the mail template', async () => {
    const textField = wrapper.find('v-text-field')
    textField.element.value = 'test';
    const activator  = (x) => {return {template: {name: x}}}
    triggerInput(textField, wrapper, activator)
    expect(wrapper.vm.$data.template.name).toBe('test');
  })

  it('sets the v-model of v-textarea for the text of the mail template', async () => {
    const textArea = wrapper.find('v-textarea')
    textArea.element.value = 'Dit is een test mail template #test#';
    const activator  = (x) => {return {template: {text: x}}}
    triggerInput(textArea, wrapper, activator)
    expect(wrapper.vm.$data.template.text).toBe('Dit is een test mail template #test#');
  })

  it('opens the dialog when the information icon is clicked', async () => {
    const infoIcon = wrapper.find('v-icon');
    infoIcon.trigger('click');
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.showDialog).toBe(true);
  });

  it('test if createTemplate is called when the create button is clicked', async () => {
    CreateEditMailTemplate.methods.createTemplate = jest.fn()
    const wrapper = mount(CreateEditMailTemplate)
    await wrapper.setData({template: {name: 'test', text: 'Dit is een test mail template #test#'}})
    await wrapper.vm.$nextTick();

    const saveButton = wrapper.find('[data-test="create-button"]');
    await saveButton.trigger('click');
    await wrapper.vm.$nextTick();


    expect(CreateEditMailTemplate.methods.createTemplate).toHaveBeenCalled();
  });

  it('test if editTemplate is called when the edit button is clicked', async () => {
    CreateEditMailTemplate.methods.editTemplate = jest.fn()
    const wrapper = mount(CreateEditMailTemplate)
    await wrapper.setProps({edit: true})
    await wrapper.setData({template: {name: 'test', text: 'Dit is een test mail template #test#'}})
    await wrapper.vm.$nextTick();

    const saveButton = wrapper.find('[data-test="edit-button"]');
    await saveButton.trigger('click');
    await wrapper.vm.$nextTick();


    expect(CreateEditMailTemplate.methods.editTemplate).toHaveBeenCalled();
  });


})
