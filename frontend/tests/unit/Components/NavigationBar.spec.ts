import {mount} from "@vue/test-utils";
import NavigationBar from "@/components/NavigationBar.vue";

describe('NavigationBar.vue', () => {

  let wrapper;
  let logout;

  beforeEach(() => {
    NavigationBar.beforeCreate = () => Promise.resolve();
    logout = jest.fn();
    wrapper = mount(NavigationBar, {
      setup() {
        return {
          logout
        }
      }
    });
  });

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('test for different routes no admin', () => {
    expect(wrapper.find('[data-test="list"]').exists()).toBeTruthy();
    expect(wrapper.vm.$data.isAdminOrSu).toBeFalsy();

    expect(wrapper.find('[data-test="home"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="account"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="logout"]').exists()).toBeTruthy();
  })

  it('test for routes admin', async () => {
    await wrapper.setData({isAdminOrSu: true});
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.$data.isAdminOrSu).toBeTruthy();

    expect(wrapper.find('[data-test="home"]').exists()).toBeFalsy();

    expect(wrapper.find('[data-test="dashboard"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="templates"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="locations"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="rounds"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="buildings"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="student"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="syndicus"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="emails"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="account"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="logout"]').exists()).toBeTruthy();
  });

  it('log-out user', async () => {
    const logoutListItem = wrapper.find('[data-test="logout"');
    await logoutListItem.trigger('click');
    expect(logout).toHaveBeenCalled();
  });


});
