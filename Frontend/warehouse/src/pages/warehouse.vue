<template>
<div id="warehouse global-bg-color">
  <GoBack v-bind:target="target"/>
  <div class="top-div global-bg-color">
    <el-row style="width: 100%">
      <el-col :span="(index > 0 && index == utilizationRateList.length - 1) ? 6 : 3" v-for="(item, index) in utilizationRateList" :key="index">
        <el-row v-for="(subItem, subIndex) in item.list" :key="subIndex" class="item-row">
          <el-col :span="15" class="subItem-left-col"><div>{{subIndex}}</div></el-col>
          <el-col :span="9" class="subItem-right-col"><div :class="{'green':subIndex === specialKey}">{{item.list[subIndex]}}</div></el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>

  <div v-if="type === '1'">
    <div class="special-content-div global-bg-color">
      <el-row v-for="(item, index) in storagebinList" :key="index" class="storage-col">
        <el-col class="storage-left-col">{{item.name}}</el-col>
        <el-col class="storage-right-col">
          <span v-for="(subItem, subIndex) in item.list" :key="subIndex">
            <br v-if="isShowBr(item, subIndex)">
            <div class="div-null" v-if="isShowNullDiv(item, subIndex)"></div>
            <el-button class="storage-item-btn"
                       :class="btnClass(subItem.status)"
                       @click="redirect(subItem.name)">
              {{subItem.name}}
            </el-button>
          </span>
        </el-col>
      </el-row>
    </div>
  </div>
  <div v-else>
    <div class="content-div global-bg-color">
      <el-row style="width: 100%" :gutter="10">
        <el-col :span="4" v-for="(item, index) in storagebinList" :key="index" style="margin-bottom: 10px">
          <el-button class="storagebin-btn"
                     :class="btnClass(item.status)"
                     @click="redirect(item.name)">
            {{item.name}}
          </el-button>
        </el-col>
      </el-row>
    </div>
  </div>

</div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'warehouse',
    data() {
      return {
        target: '/plan',
        utilizationRateList: [],
        storagebinList: [],
        type: '',
        specialKey: '2-使用率',
        specialArray: ['02-05', '02-04', '02-03', '03-05', '03-04', '03-03', '05-05', '05-04', '05-03']
      }
    },
    methods: {
      init() {
        this.type = this.$route.params.type
        let reqParams = {
          warehouse_type: this.type
        }
        console.log("params:" + JSON.stringify(reqParams))
        this.$axios.get('/api/v1000/elevated/utilization_rate', {params : reqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            data.forEach((item, index) => {
              let list = item.list
              for (let key in list) {
                let value = list[key];
                if (key === this.specialKey) {
                  let pValue = (value*100).toPrecision(12);
                  pValue = parseFloat(pValue).toFixed(2);
                  value = pValue + '%';
                  list[key] = value
                }
                data[index] = item
              }
            })
            this.utilizationRateList = data
          }
        })
        this.$axios.get('/api/v1000/elevated/storagebin', {params : reqParams}).then(res => {
          let data = res.data
          // console.log("storagebin:" + JSON.stringify(data))
          if (data && data.length > 0) {
            if (this.type === '1') {
              data.forEach((item, index) => {
                let list = item.list;
                list.sort(this.sortBy('name'));
              })
            }
            this.storagebinList = data
          }
        })
      },
      redirect(binum) {
        console.log("binum:" + binum + ",type:" + this.type)
        this.$router.push(`/detail/${this.type}/${binum}/warehouse`)
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
      },
      sortBy (field) {
        return function(a, b) {
          let value1 = a[field].substring(3, 5);
          let value2 = b[field].substring(3, 5);
          return value2 - value1;
        }
      },
      isShowBr(item, subIndex) {
        let list = item.list
        let currName = list[subIndex].name.substring(0, 5);
        let lastName = list[subIndex > 0 ? subIndex - 1 : 0 ].name.substring(0, 5);
        if (currName !== lastName) {
          return true
        }
        return false
      },
      isShowNullDiv(item, subIndex) {
        let list = item.list

        let curr = list[subIndex].name
        let currName = curr.substring(curr.length - 2)

        let last = list[subIndex > 0 ? subIndex - 1 : 0 ].name
        let lastName = last.substring(last.length - 2)

        let flag = false
        if (currName === '02' && lastName !== '01') {
          flag = true
        }
        return flag
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
  .special-content-div {
    width: 4000px;
    padding: 30px;
    .storage-col {
      margin-bottom: 30px;
      .storage-left-col {
        width: 130px;
        text-align: right;
        margin-right: 20px;
        font-size: 18px;
        font-weight: 600;
        color: #333333;
      }
      .storage-right-col {
        width: calc(~"100% - 150px");
        .storage-item-btn {
          margin: 0 5px 5px 0;
        }
        .div-null {
          width: 100px;
          margin: 2px;
          display: inline-block;
        }
      }
    }
  }
  .top-div {
    display: flex;
    padding: 30px;
  }
  .content-div {
    /*margin-top: 50px;*/
    /*width: 4000px;*/
    padding: 30px;
    .storagebin-btn {
      width: 100%;
      height: 90px;
      font-size: 30px;
      font-weight: 600;
    }
  }
  .item-row {
    line-height: 40px;
    font-size: 18px;
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
  .top-div {
    .el-col-3 {
      width: 13.8%;
      .item-row {
        font-weight: 500;
      }
    }
    .el-col-6 {
      width: 17%;
      padding-left: 50px;
      .item-row {
        font-weight: 800;
      }
    }
    .el-col-9 {
      width: 40%;
    }
    .el-col-15 {
      width: 60%;
    }
  }
  .green {
    background-color: #19ce50;
  }
</style>
