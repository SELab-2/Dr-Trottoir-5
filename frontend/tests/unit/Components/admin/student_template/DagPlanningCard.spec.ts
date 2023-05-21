import {mount} from "@vue/test-utils";
import DagPlanningCard from "@/components/admin/student_template/DagPlanningCard.vue"

describe('DagPlanningCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    DagPlanningCard.methods.remove_dagplanning = jest.fn()
    wrapper = mount(DagPlanningCard);
  })

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('check if the data gets rendered without "Vervaning"', async () => {
    await wrapper.setProps({
      data: {
        template_id: 1,
        ronde_id: 1,
        status: "Actief",
        dag_id: 0,
        students: [{first_name: 'Test'}],
        day: 'MO',
        start_hour: '17:00',
        end_hour: '20:00'
      }
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="students"]').text()).toBe('Test');
    expect(wrapper.find('[data-test="format"]').text()).toBe('Maandag');
    expect(wrapper.find('[data-test="start-hour"]').text()).toBe('17:00    -');
    expect(wrapper.find('[data-test="end-hour"]').text()).toBe('20:00');
    expect(wrapper.find('[data-test="edit"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="remove-button"]').exists()).toBeTruthy();

    expect(wrapper.find('[data-test="message"]').exists()).toBeFalsy();
  });

  it('test delete button', async () => {
    const deleteButton = wrapper.find('[data-test="remove-button"]');
    expect(deleteButton.exists()).toBeTruthy();
    await deleteButton.trigger('click');
    expect(DagPlanningCard.methods.remove_dagplanning).toHaveBeenCalled();
  })

  it('vervanging render', async () => {
    await wrapper.setProps({
      data: {
        template_id: 1,
        ronde_id: 1,
        status: "Vervangen",
        dag_id: 0,
        students: [{first_name: 'Test'}],
        day: 'MO',
        start_hour: '17:00',
        end_hour: '20:00'
      }
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="edit"]').exists()).toBeFalsy();
    expect(wrapper.find('[data-test="remove-button"]').exists()).toBeFalsy();

    expect(wrapper.find('[data-test="message"]').exists()).toBeTruthy();
  })

});
