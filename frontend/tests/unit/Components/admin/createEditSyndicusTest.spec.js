import {mount} from '@vue/test-utils'
import CreateEditSyndicus from "@/components/admin/CreateEditSyndicus.vue";

describe('CreateEditSyndicus.vue', () => {
  let wrapper;

  beforeEach(() => {
    CreateEditSyndicus.mounted = jest.fn()
    wrapper = mount(CreateEditSyndicus)
  })


  it('renders props.msg when passed', () => {
    expect(wrapper.exists()).toBe(true);
    expect(CreateEditSyndicus.mounted).toHaveBeenCalled();
  })

  it('show right title', async () => {
    expect(wrapper.find('h1').text()).toBe('Maak nieuwe Syndicus aan');
    await wrapper.setProps({edit: true});
    await wrapper.vm.$forceUpdate();
    expect(wrapper.find('h1').text()).toBe('Syndicus aanpassen');
  })

  it('call addSyndicus when submit', async () => {
    CreateEditSyndicus.methods.addSyndicus = jest.fn();
    wrapper = mount(CreateEditSyndicus);
    const button = await wrapper.find('[data-test="add"]')
    await button.trigger('click');
    expect(CreateEditSyndicus.methods.addSyndicus).toHaveBeenCalled();
  })

  it('call editSyndicus when submit', async () => {
    CreateEditSyndicus.methods.editSyndicus = jest.fn();
    wrapper = mount(CreateEditSyndicus, {
      propsData: {
        edit: true
      }
    });
    const button = await wrapper.find('[data-test="edit"]')
    await button.trigger('click');
    expect(CreateEditSyndicus.methods.editSyndicus).toHaveBeenCalled();
  })

  it('render component correctly', () => {
    const labels = wrapper.findAll('label');
    expect(labels.length).toBe(3);
    expect(labels.at(0).text()).toBe('Syndicus');
    expect(labels.at(1).text()).toBe('Locatie');
    expect(labels.at(2).text()).toBe('Gebouwen');

    expect(wrapper.findAll('v-autocomplete').length).toBe(3);
  })
})
