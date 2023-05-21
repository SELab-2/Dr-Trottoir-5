import {mount} from "@vue/test-utils";
import TemplateRondeCard from "@/components/admin/student_template/TemplateRondeCard.vue";

describe('TemplateRondeCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    TemplateRondeCard.methods.on_delete = jest.fn();
    wrapper = mount(TemplateRondeCard);
  });

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('render of data', async () => {
    await wrapper.setProps({
      data: {
        template_id: 0,
        ronde_id: 0,
        status: "Actief",
        name: 'Test Template Ronde',
        location: 'Gent'
      }
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="location"]').text()).toBe('Gent');
    expect(wrapper.find('[data-test="name"]').text()).toBe('Test Template Ronde');

    expect(wrapper.find('[data-test="dagplanning-button"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="delete-button"]').exists()).toBeTruthy();
  });

  it('delete template', async () => {
    const deleteButton = wrapper.find('[data-test="delete-button"]');
    await deleteButton.trigger('click');
    expect(TemplateRondeCard.methods.on_delete).toHaveBeenCalled();
  });

  it('template can not delete', async () => {
    await wrapper.setProps({
      data: {
        template_id: 0,
        ronde_id: 0,
        status: "Vervangen",
        name: 'Test Template Ronde',
        location: 'Gent'
      }
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="delete-button"]').exists()).toBeFalsy();
  })

});
