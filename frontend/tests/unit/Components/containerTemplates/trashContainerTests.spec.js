import {mount} from '@vue/test-utils';
import TrashContainerCard from "@/components/containerTemplates/containers/TrashContainerCard.vue";

describe('trashContainerCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashContainerCard.beforeMount = jest.fn();
    TrashContainerCard.methods.editContainer = jest.fn();
    TrashContainerCard.methods.deleteContainer = jest.fn();
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

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashContainerCard.beforeMount).toBeCalled();

    expect(wrapper.find('.container-border').exists()).toBe(true);
    expect(wrapper.find('v-row[align="center"][justify="center"]').exists()).toBe(true);
    expect(wrapper.findAll('v-col').length).toBe(6);

    expect(wrapper.find('v-col:nth-child(1) p.text-style-title').text()).toBe('Monday');
    expect(wrapper.find('v-col:nth-child(2) p').text()).toBe('10 AM - 12 PM');
    expect(wrapper.find('v-col:nth-child(3) p').text()).toBe('Type A');

    expect(wrapper.find('v-col:nth-child(5) .button-style').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(6) .button-style').exists()).toBe(true);
  });

  it('edit button is called', async () => {
    const editButton = wrapper.find('[data-test="edit"]');
    await editButton.trigger('click');
    expect(TrashContainerCard.methods.editContainer).toBeCalled();
  })

  it('delete button is called', async () => {
    const deleteButton = wrapper.find('[data-test="delete"]');
    await deleteButton.trigger('click');
    expect(TrashContainerCard.methods.deleteContainer).toBeCalled();
  })

})
