<template>
  <div id="app">
    <v-app>
      <v-content>
        <v-container class="main-container">

          <v-tabs
            color="blue darken-4"
            dark
            slider-color="cyan"
            right
          >
            <v-tab>
              <router-link to="/" class="link">Home</router-link>
            </v-tab>
            <v-tab>
              <router-link to="/monitoring" class="link">Monitoring</router-link>
            </v-tab>
            <v-tab float="right">
              <router-link to="/settings" class="link">
                <v-btn flat icon color="cyan">
                  <v-icon>settings</v-icon>
                </v-btn>
              </router-link>
            </v-tab>
          </v-tabs>

          <router-view></router-view>
        </v-container>
      </v-content>
    </v-app>

    <img src="./assets/vue-logo.png">
    <img id="django" src="./assets/django-logo.png">
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import Settings from './components/Settings'
  import Monitoring from './components/Monitoring'
  import Home from './components/Home'

  Vue.use(VueRouter)

  var router = new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', component: Home },
      { path: '/monitoring', component: Monitoring },
      { path: '/settings', component: Settings }
    ]
  })

  module.exports = {
    name: 'app',

    router: router,

    components: {
      Settings,
      Monitoring
    }

  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    width: 100%;
    height: 100%;
  }
  #django {
    max-width:30%;
    height:auto;
  }

  .main-container {
    padding: 0;
  }

  .link {
    color: white;
    text-decoration: none;
  }
</style>
