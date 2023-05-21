import {mount} from "@vue/test-utils";
import StudentTemplateCard from "@/components/admin/student_template/StudentTemplateCard.vue";

describe('StudentTemplateCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    StudentTemplateCard.methods.delete_template = jest.fn();
    wrapper = mount(StudentTemplateCard);
  });

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  });

  it('render of data', async () => {
    await wrapper.setProps({
      data: {
        template_id: 0,
        name: 'Test template',
        location: 'Gent',
        even: true,
        status: 'Actief'
      }
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="location"]').text()).toBe('Gent');
    expect(wrapper.find('[data-test="even"]').text()).toBe('even');
    expect(wrapper.find('[data-test="name"]').text()).toBe('Test template');
    expect(wrapper.find('[data-test="status"]').text()).toBe('Actief');

    expect(wrapper.find('[data-test="edit"]').exists()).toBeTruthy()
    expect(wrapper.find('[data-test="delete-button"]').exists()).toBeTruthy()

    expect(wrapper.find('[data-test="message"]').exists()).toBeFalsy()
  });

  it('delete template', async () => {
    const deleteButton = wrapper.find('[data-test="delete-button"]');
    await deleteButton.trigger('click');
    expect(StudentTemplateCard.methods.delete_template).toHaveBeenCalled();
  });

  it('vervangen render', async () => {
    await wrapper.setProps({
      data: {
        template_id: 0,
        name: 'Test template',
        location: 'Gent',
        even: true,
        status: 'Vervangen'
      }
    });
    await wrapper.vm.$nextTick();

    expect(wrapper.find('[data-test="edit"]').exists()).toBeFalsy()
    expect(wrapper.find('[data-test="delete-button"]').exists()).toBeFalsy()

    expect(wrapper.find('[data-test="message"]').exists()).toBeTruthy()
  })

});
