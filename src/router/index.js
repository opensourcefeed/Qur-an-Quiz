import Vue from 'vue'
import Router from 'vue-router'
import Menu from '@/components/Menu'
import Chapter from '@/components/Chapter'
import Question from '@/components/Question'
import Result from '@/components/Result'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Menu',
      component: Menu
    },
    {
      path: '/chapter',
      name: 'Chapter',
      component: Chapter
    },
    {
      path: '/chapter/:chapter/question/:number?',
      name: 'Question',
      component: Question
    },
    {
      path: '/quiz/result',
      name: 'Result',
      component: Result
    }
  ]
})
