import Vuex from 'vuex'
import Vue from 'vue'
import { get, post } from '../utils/api'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    items: [], // 用户参加的活动
    user: {},
    messages: [], // 用户消息
    globalItems: [] // 所有活动
  },
  getters: {
    'getItemById': (state) => {
      return function (id) {
        return state.items.filter((item) => {
          return item.id === id
        })[0]
      }
    },
    'getMessageById': (state) => {
      return function (id) {
        return state.messages.filter((item) => {
          return item.id === id
        })[0]
      }
    },
    'getGlobalItemById': (state) => {
      return function (id) {
        return state.globalItems.filter((item) => {
          return item.id === id
        })[0]
      }
    }
  },
  mutations: {
    getItems (state) {
      get({ 'url': '/users/123/activities' }).then((res) => {
        state.items = res
      })
    },
    getMessages (state) {
      get({ 'url': '/users/123/messages' }).then((res) => {
        state.messages = res
        state.messages.forEach(elem => {
          elem.decription = elem.content.slice(0, 20) + '...'
        })
      })
    },
    changeIsRead (state, id) {
      state.messages.forEach(elem => {
        if (elem.id === id) {
          elem.isRead = true
          post({'url': `/messages/${elem.id}/`, 'data': elem})
        }
      })
    },
    getUser (state, id) {
      get({'url': '/users/123'}).then(res => {
        state.user = res
        console.log(state.user)
      })
    },
    logIn (state, data) {
      post({'url': '/auth/login', 'data': {'schoolId': data.schoolId, 'password': data.password}}).then(res => {
        state.user = res
      })
    },
    changeInfo (state, info) {
      for (let k in info) {
        state.user[k] = info[k]
      }
      post({'url': `/users/${state.user.id}`, 'data': state.user})
    },
    getGlobalItems (state) {
      get({'url': '/activities'}).then(res => {
        state.globalItems = res
      })
    },
    applyItem (state, data) {
      console.log('apply')
    }
  }
})

export default store
