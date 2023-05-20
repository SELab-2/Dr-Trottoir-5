import { mount } from '@vue/test-utils'
import CreateEditRoundView from '@/views/admin/CreateEditRoundView.vue'

describe('CreateEditRoundView.vue', () => {

  let wrapper;

  beforeEach(() => {
    CreateEditRoundView.beforeCreate = jest.fn();
    wrapper = mount(CreateEditRoundView);
  })

  it('renders the correct', () => {
    expect(wrapper.exists()).toBe(true);
    expect(CreateEditRoundView.beforeCreate).toHaveBeenCalled();
  })

  it('renders the correct title when id is undefined', () => {
    const title = wrapper.find('h4.text-h4');
    expect(title.text()).toBe('Nieuwe ronde aanmaken');
  });

  it('renders the correct title when id is defined', () => {
    const wrapper = mount(CreateEditRoundView, {
      propsData: {
        id: '123'
      }
    });
    const title = wrapper.find('h4.text-h4');
    expect(title.text()).toBe('Ronde bewerken');
  });

  it('calls createRound method when "Aanmaken" button is clicked', async () => {
    CreateEditRoundView.methods.createRound = jest.fn();
    wrapper = mount(CreateEditRoundView);
    const createButton = wrapper.find('[data-test="create"]');
    await createButton.trigger('click');
    expect(CreateEditRoundView.methods.createRound).toHaveBeenCalled();
  });

  it('calls createRound method when "Opslaan" button is clicked', async () => {
    CreateEditRoundView.methods.createRound = jest.fn();
    const wrapper = mount(CreateEditRoundView, {
      propsData: {
        id: '123'
      }
    });
    const saveButton = wrapper.find('[data-test="save"]');
    await saveButton.trigger('click');
    expect(CreateEditRoundView.methods.createRound).toHaveBeenCalled();
  });

  it('renders the component correctly', async() => {
    expect(wrapper.find('v-autocomplete[label="Locatie"]').exists()).toBeTruthy();
    expect(wrapper.find('v-autocomplete[label="Gebouwen"]').exists()).toBeTruthy();
  })
})
