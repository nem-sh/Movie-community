import Vue from 'vue'
import VueRouter from 'vue-router'
import ProfileView from '../views/accounts/ProfileView.vue'

import ProfileUpdateView from '../views/accounts/ProfileUpdateView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import MovieListView from '../views/boards/MovieListView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import MovieDetailView from '../views/boards/MovieDetailView'
import MovieReviewCreateView from '../views/boards/MovieReviewCreateView.vue'
import MovieReviewDetailView from '../views/boards/MovieReviewDetailView.vue'
import MovieReviewUpdateView from '../views/boards/MovieReviewUpdateView.vue'
import CommunityView from '../views/boards/CommunityView.vue'

import MovieView from '../views/boards/MovieView.vue'

import SearchView from '../views/boards/SearchView'
Vue.use(VueRouter)

  const routes = [
    {
      path: '/accounts/profile/:userId/',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/accounts/profile_update/:userId/',
      name: 'ProfileUpdate',
      component: ProfileUpdateView,
    },
    {
      path: '/accounts/signup',
      name: 'Signup',
      component: SignupView,
    },
    {
      path: '/accounts/login',
      name: 'Login',
      component: LoginView,
    },

    {
      path: '/boards',
      name: 'MovieList',
      component: MovieListView,
    },

    {
      path: '/boards/community',
      name: 'community',
      component: CommunityView,
    },
    {
      path: '/boards/movie',
      name: 'movie',
      component: MovieView,
    },

    {
      path: '/boards/:movieId',
      name: 'MovieDetail',
      component: MovieDetailView,
    },
    {
      path: '/boards/:movieId/review_create',
      name: 'MovieReviewCreate',
      component: MovieReviewCreateView,
    },
    {
      path: '/boards/:movieId/:reviewId',
      name: 'MovieReviewDetail',
      component: MovieReviewDetailView,
    },
    {
      path: '/boards/:movieId/:reviewId/review_update',
      name: 'MovieReviewUpdate',
      component: MovieReviewUpdateView,
    },
    {
      path: '/search',
      component: SearchView,
    },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
