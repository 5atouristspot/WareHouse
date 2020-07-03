<template>
  <div id="search">
    <GoBack v-bind:target="target"/>
    <div class="content-div global-bg-color">
      <div class="search-div">
        <el-input
          class="search-input"
          placeholder="请输入内容"
          prefix-icon="el-icon-search"
          clearable="true"
          v-model="input">
        </el-input>
        <el-button type="primary" icon="el-icon-search">搜索</el-button>
      </div>

    </div>
  </div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'search',
    data() {
      return {
        target: '/plan',
        input: ''
      }
    },
    methods: {
      init() {

      }
    },
    components: {
      GoBack: GoBack
    },
    created() {
      this.init()
    }
  }
</script>

<style lang="less" scoped>
  .content-div {
    width: 100%;
    .search-input {
      width: 350px;
      margin-right: 20px;
    }
  }
</style>
