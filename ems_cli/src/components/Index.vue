<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2009/11/20
            <br/>
            <a href=" " @click="quit">安全退出</a>
<!--            <router-link to="/login" @click="quit">安全退出</router-link>-->
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          Welcome!欢迎{{this.name}}来到管理系统
        </h1>
        <table class="table">
          <tr class="table_header">
            <td>ID</td>
            <td>Name</td>
            <td>Photo</td>
            <td>Salary</td>
            <td>Age</td>
            <td>Operation</td>
          </tr>
          <tr class="row2" v-for="emp in emp_list" :key="emp.id">
            <td>{{ emp.id }}</td>
            <td>{{ emp.emp_name }}</td>
            <td><img :src=emp.full_img style="height: 60px;width: 60px"></td>
            <td>{{ emp.salary }}</td>
            <td>{{ emp.age }}</td>
            <td>
              <el-button @click="del_emp(emp.id)" type="text" size="small">删除员工</el-button>
              <el-button @click="update_emp(emp.id)" type="text" size="small">更新员工</el-button>
            </td>
          </tr>
        </table>
        <p>
          <el-button type="primary">
            <router-link to="/add">添加员工</router-link>
          </el-button>
        </p>
      </div>
    </div>
    <div id="footer">
      <div id="footer_bg">
        ABC@126.com
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Index",
  data() {
    return {
      emp_list: [],
      name:sessionStorage.getItem('username')
    }
  },
  methods: {
    get_all_emp() {
      let username = sessionStorage.getItem("username")
      if (username) {
        this.$axios.get("http://127.0.0.1:8000/userapp/employees/").then(res => {

          this.emp_list = res.data;
        }).catch(error => {
          //console.log(error);
        })
      } else {
        this.$message.error("当前用户未登录,请登录");
        this.$router.push("/login");
      }
    },
    update_emp(id) {
      //console.log(id);
      this.$router.push("/update/" + id)
    },
    del_emp(id){
      this.$axios({
        url: "http://127.0.0.1:8000/userapp/employees/" +id,
        method: "delete",
      }).then(res => {
        this.$router.go(0);
      })

    },
    quit(){
      sessionStorage.clear()
    }
  },
  created() {
    this.get_all_emp();
  }
}
</script>

<style scoped>

</style>
