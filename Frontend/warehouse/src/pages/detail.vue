<template>
<div id="detail">
  <GoBack v-bind:target="target"/>
  <div class="detail-content global-bg-color">
    <el-row class="item-row" v-for="(item, index) in detailList" :key="index">
      <div v-if="item.name === '0-material'" style="overflow: hidden;">================================================================================================================================================================================================================================================</div>
      <el-col :span="4" class="subItem-left-col"><div>{{item.name}}</div></el-col>
      <el-col :span="6" class="subItem-right-col"><div>{{item.value}}</div></el-col>
    </el-row>
  </div>
</div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'detail',
    data() {
      return {
        target: '',
        binum: '',
        type: '',
        batchType: '',
        detailList: []
      }
    },
    methods: {
      init() {
        this.type = this.$route.params.type
        this.binum = this.$route.params.binum
        if (this.type === 'batch') {
          this.batchType = this.$route.params.batchType
          this.target = '/batch/' + this.batchType

          let reqParams = {
            batch_type: this.batchType,
            batchnum: this.binum
          }
          console.log("params:" + JSON.stringify(reqParams))
          this.$axios.get('/api/v1000/elevated/batchdetail', {params : reqParams}).then(res => {
            let data = res.data
            if (data && data.length > 0) {
              this.detailList = data
            }
          })

        } else {
          this.target = '/warehouse/' + this.type

          let reqParams = {
            binum: this.binum
          }
          console.log("params:" + JSON.stringify(reqParams))
          this.$axios.get('/api/v1000/elevated/storagedetail', {params : reqParams}).then(res => {
            let data = res.data
            if (data && data.length > 0) {
              this.detailList = data
            }
          })
        }

      },

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
.detail-content {
  padding: 30px 30px 0 30px;
  .item-row {
    line-height: 50px;
    font-size: 20px;
    font-weight: 600;
    padding: 2px 0 2px 0;
    color: #000000;
    div{
      border-radius: 4px;
    }
  }
  .subItem-left-col {
    text-align: right;
    background-color: #d3dce6;
    padding-right: 10px;
  }
  .subItem-right-col {
    padding: 0 5px 0 5px;
    div {
      padding-left: 10px;
    }
  }
}
</style>
