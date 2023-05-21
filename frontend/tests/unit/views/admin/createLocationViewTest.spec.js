import { mount } from '@vue/test-utils'
import CreateLocationView from '@/views/admin/CreateLocationView.vue'
import {triggerInput} from "../../../utils/testHelper";

describe('CreateLocationView.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateLocationView);
  })

  it('renders the correct', () => {
    expect(wrapper.exists()).toBe(true);
  })

  it('initializes data correctly', () => {
    expect(wrapper.vm.name).toBe('');
    expect(wrapper.vm.errors).toBe(null);
  });

  it('calls addLocation method on button click', async () => {
    CreateLocationView.methods.addLocation = jest.fn();
    wrapper = mount(CreateLocationView);
    await wrapper.find('[data-test="add"]').trigger('click');

    expect(CreateLocationView.methods.addLocation).toHaveBeenCalled();
  });

  it('renders the component correctly', async() => {
    const h1s = wrapper.findAll('h1');
    expect(h1s.at(0).text()).toBe('Nieuwe locatie aanmaken');
    expect(h1s.at(1).text()).toBe('Naam');
  })

  it('updates name when v-model is changed', async () => {
    const input = wrapper.find('v-text-field');
    input.element.value = 'New Location';
    const activator = (x) => {
      return {name: x}
    }
    triggerInput(input, wrapper, activator)

    expect(wrapper.vm.name).toBe('New Location');
  });
})
