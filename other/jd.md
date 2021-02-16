



## 1.[项目]() 

##  2.rocketmq应该用于在哪些地方，消费方出现问题怎么办。 

异步 削峰 解耦

## 3.限流如何实现 

限流三种方式：合法性验证限流，容器限流，服务端限流

容器限流：tomcat设置最大线程数

nginx限流：

控制速率： 限制每个ip的访问频率

和控制并发连接数：单个ip链接和总链接

服务端限流算法：时间窗口 漏桶 

## 4.springMVC你知道的注解，[前端]()如果有个奇怪的时间字符串，如果解析（使用springMVC注解实现） 

@Controller

@RequestMapping

@Resource

@Autowired

@Repository

@ResponseBody

https://www.cnblogs.com/leskang/p/5445698.html

##  5.HashMap和TreeMap区别 

TreeMap有序

## 6.HashMap如何遍历，TreeMap如果[排序]()的 

foreach

Iterator

 ## 7.lambda表达式和foreach区别，stream了解嘛 

## 8.给你一个字符串（以“,”分隔），用lambda表达式将字符串解析成List 

```java
ArrayList<String> list = new ArrayList<>(Arrays.asList("I", "love", "you", "too"));
list.forEach( str -> {
        if(str.length()>3)
            System.out.println(str);
    });


import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>(Arrays.asList("I", "love", "you", "too"));
        list.forEach( str -> {
            if(str.length()>3)
                System.out.println(str);
        });
        String s  = "1,2,3,4,5";
        Stream<String> stream = Stream.of(s);
        List<String> collect = Stream.of(s.split(",")).collect(Collectors.toList());
        String s1 = collect.stream().collect(Collectors.joining(","));
        System.out.println(s1);
    }
}

```



  9.JDK8的时间类了解吗 

  10.线程池的阻塞队列出队方式有哪些。缓存线程池了解吗。 

  11.liunx如果通过名字查端口/进程



