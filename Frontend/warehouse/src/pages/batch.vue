<template>
<div id="batch">
  <GoBack v-bind:target="target"/>
  <div class="content-div global-bg-color">
    <el-row style="width: 100%" :gutter="10">
      <el-col :span="4" v-for="(item, index) in batchList" :key="index" style="margin-bottom: 10px">
        <el-button @click="redirect(item.batch)"
                   class="batch-btn"
                   :class="btnClass(item.status)">
          {{item.batch}}
        </el-button>
      </el-col>
    </el-row>
  </div>
</div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'batch',
    data() {
      return {
        target: '/plan',
        type: '',
        batchList: []
      }
    },
    methods: {
      init() {
        this.type = this.$route.params.type
        let reqParams = {
          batch_type: this.type
        }
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/batchinfo', {params : reqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            this.batchList = data
          }
        })

      },
      redirect(batchnum) {
        this.$router.push(`/detail/batch/${batchnum}/status/${this.type}`)
      },
      btnClass(status) {
        let btnClazz = 'white-btn'
        if (status === 'Q') {
          btnClazz = 'red-btn'
        } else if (status === 'S') {
          btnClazz = 'yellow-btn'
        } else if (status === '') {
          btnClazz = 'green-btn'
        }
        return btnClazz
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
    /*margin-top: 50px;*/
    /*width: 4000px;*/
    padding: 30px;
    .batch-btn {
      width: 100%;
      height: 90px;
      font-size: 30px;
      font-weight: 600;
    }
  }
</style>
