import { mount } from '@vue/test-utils';
import TrashContainerCard from "@/components/containerTemplates/containers/TrashContainerCard.vue";

describe('trashContainerCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashContainerCard.beforeMount = jest.fn();
    wrapper = mount(TrashContainerCard, {
      propsData: {
        data: {
          trash_container: {
            collection_day: {
              day: 'Monday',
              start_hour: '10 AM',
              end_hour: '12 PM',
            },
            type: 'Type A',
          },
          extra_id: 1,
        },
      },
    });
  })

  it('render', () => {
    expect(wrapper.exists()).toBe(true);
  })
})
