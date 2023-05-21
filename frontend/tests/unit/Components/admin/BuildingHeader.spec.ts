import {mount} from "@vue/test-utils"
import BuildingHeader from "@/components/admin/BuildingHeader.vue"

describe('BuildingHeader.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(BuildingHeader);
  })

  it('render of comonent', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('check field are present', async () => {
    await wrapper.setProps({round: true});
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="title"]').text()).toBe('Gebouw')
    expect(wrapper.find('[data-test="adres"]').text()).toBe('Adres')
    expect(wrapper.find('[data-test="round"]').exists()).toBeFalsy();
    expect(wrapper.find('[data-test="manual"]').text()).toBe('Handleiding');
    expect(wrapper.find('[data-test="status"]').text()).toBe('Document status')
  });

  it('test for round',  () => {
    expect(wrapper.find('[data-test="round"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="round"]').text()).toBe('Efficiëntie')
  })

})
