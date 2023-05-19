import {mount} from '@vue/test-utils';
import StateButtons from "@/components/StateButtons.vue";

describe('StateButtons.vue', function () {
  it('renders the correct buttons when status is "A"', () => {
    const wrapper = mount(StateButtons, {
      propsData: {
        eenmalig: jest.fn(),
        permanent: jest.fn(),
        status: 'A',
      },
    });

    expect(wrapper.find('.bg-secondary').exists()).toBe(true);
    expect(wrapper.find('.bg-primary').exists()).toBe(true);
    expect(wrapper.find('.text-primary').exists()).toBe(true);
    expect(wrapper.find('.text-secondary').exists()).toBe(true);
  });

  it('renders the correct buttons when status is "E"', () => {
    const wrapper = mount(StateButtons, {
      propsData: {
        eenmalig: jest.fn(),
        permanent: jest.fn(),
        status: 'E',
      },
    });

    expect(wrapper.find('.bg-primary').exists()).toBe(true);
    expect(wrapper.find('.text-secondary').exists()).toBe(true);
  });

  it('renders the correct message when status is "V"', () => {
    const wrapper = mount(StateButtons, {
      propsData: {
        eenmalig: jest.fn(),
        permanent: jest.fn(),
        status: 'V',
      },
    });

    expect(wrapper.find('.text-caption').exists()).toBe(true);
  });

  it('emits the correct events when buttons are clicked status A', () => {
    const eenmaligMock = jest.fn();
    const permanentMock = jest.fn();
    const wrapper = mount(StateButtons, {
      propsData: {
        eenmalig: eenmaligMock,
        permanent: permanentMock,
        status: 'A',
      },
    });

    const eenmalig = wrapper.find('.bg-secondary')
    eenmalig.trigger('click');
    expect(eenmaligMock).toHaveBeenCalledTimes(1);
    expect(eenmalig.text()).toBe('Eenmalig aanpassen')

    const permanent = wrapper.find('.bg-primary')
    permanent.trigger('click');
    expect(permanentMock).toHaveBeenCalledTimes(1);
    expect(permanent.text()).toBe('Permanent aanpassen')
  });

  it('emits the correct events when buttons are clicked status E', () => {
    const eenmaligMock = jest.fn();
    const permanentMock = jest.fn();
    const wrapper = mount(StateButtons, {
      propsData: {
        eenmalig: eenmaligMock,
        permanent: permanentMock,
        status: 'E',
      },
    });

    const eenmalig = wrapper.find('.bg-primary')
    eenmalig.trigger('click');
    expect(eenmaligMock).toHaveBeenCalledTimes(1);
    expect(eenmalig.text()).toBe('Aanpassing opslaan')

  });
});
