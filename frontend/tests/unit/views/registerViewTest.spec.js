import { mount } from '@vue/test-utils'
import RegisterView from "@/views/RegisterView.vue";

describe('RegisterView.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(RegisterView);
  })

  it('renders the correct', () => {
    expect(wrapper.exists()).toBe(true);
  })

  it('initializes data correctly', () => {
    expect(wrapper.vm.valid).toBe(true);
    expect(wrapper.vm.showPassword).toBe(false);
    expect(wrapper.vm.firstname).toBe('');
    expect(wrapper.vm.lastname).toBe('');
    expect(wrapper.vm.email).toBe('');
    expect(wrapper.vm.password).toBe('');
    expect(wrapper.vm.password2).toBe('');
    expect(wrapper.vm.phone_nr).toBe('');
    expect(wrapper.vm.errors).toBeNull();
  });

  it('calls apiRegister method on button click', async () => {
    RegisterView.methods.apiRegister = jest.fn();
    wrapper = mount(RegisterView);
    await wrapper.find('[data-test="register"]').trigger('click');

    expect(RegisterView.methods.apiRegister).toHaveBeenCalled();
  })

  it('render correctly', async () => {
    expect(wrapper.find('v-text-field[label="Voornaam"]').exists()).toBe(true);
    expect(wrapper.find('v-text-field[label="Achternaam"]').exists()).toBe(true);
    expect(wrapper.find('v-text-field[label="E-mail"]').exists()).toBe(true);
    expect(wrapper.find('v-text-field[label="Wachtwoord"]').exists()).toBe(true);
    expect(wrapper.find('v-text-field[label="Bevestig wachtwoord"]').exists()).toBe(true);
    expect(wrapper.find('v-autocomplete[label="Locaties"]').exists()).toBe(true);
    expect(wrapper.find('v-text-field[label="GSM-nummer"]').exists()).toBe(true);
    expect(wrapper.find('div[class="mx-1"]').exists()).toBe(true);
  })

})
