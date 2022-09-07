## CSS - FLEXBOX

**Flexbox** 는 2009 년도에 소개된 CSS 레이아웃 모델로 그 전에 이용되던 Float 레이아웃과 Position 레이아웃에 비해 컨텐츠의 자유로운 배치를 가능하게 한다.

**FBLM** (Flexible Box Layout Model, a.k.a. Flexbox) 은 1차원 콘텐츠용으로 설계된 레이아웃 모델로 크기가 다른 여러 항목을 가져와서 해당 항목에 가장 적합한 레이아웃을 반환하는 데 탁월하다.

**Flexbox** 는 사이드바 패턴에 대한 이상적인 레이아웃 모델로 사이드바와 콘텐츠의 인라인 배치를 수월하게 해주고, 남은 공간이 충분하지 않은 경우 사이드바가 새 줄로 나뉘게 해준다. 또한, 브라우저가 따라야 하는 고정 치수를 설정하는 대신 콘텐츠가 표시되는 방식을 지정하는 유연한 경계를 제공할 수 있다.

**Flexbox** 의 사용 전에는 1) 부모 요소 내부에 포함된 블록 콘텐츠를 세로로 중심부에 맞추기, 2) 사용 가능한 너비와 높이에 관계없이 하나의 컨테이너에 포함된 모든 자녀 요소가 주어진 너비와 높이를 똑같은 크기로 점유하기, 3) 다단 레이아웃에 포함된 모든 단이 서로 다른 크기의 콘텐츠를 포함하고 있더라도 동일한 높이로 채택하기가 어렵거나 불가능했다.

## CSS - FLEX LAYOUT

- 행 또는 열로 표시할 수 있다.
- 문서의 쓰기 모드를 존중한다.
- 기본적으로 한 줄이지만 여러 줄로 줄 바꿀 수 있다.
- 레이아웃의 항목이 DOM (The Document Object Model) 의 순서와 다르게 시각적으로 재정렬될 수 있다.
- 공간이 항목 내부에 분산될 수 있으므로 상위 항목의 사용 가능한 공간에 따라 더 커지고 작아질 수 있다.
- 상자 정렬 속성을 사용하여 래핑된 레이아웃의 항목 및 플렉스 라인 주위에 공간을 분배할 수 있다.
- 항목 자체를 교차 축에 정렬할 수 있다.
- 

## CSS - Build a Flex-Container

Flexbox를 사용하려면 일반 블록 및 인라인 레이아웃이 아닌 플렉스 서식 컨텍스트를 사용할 것을 선언해야 한다.



e.g.

``` css
.container {
  display: flex;
}
```

이렇게 하려면 `display` 속성을 `flex`로 변경해야 한다. 플렉스 항목의 하위 항목이 있는 블록 수준 상자를 제공하고, 플렉스 항목은 **초기 값**을 사용하여 일부 Flexbox 동작을 즉시 나타내기 시작한다.



## CSS - Flexbox Layout guide

1. `justify-content` - Flex 요소들을 가로선 상에서 정렬

```
flex-start (default) , flex-end , center , space-between , space-around ,  space-evenly
```



2. `align-items` - Flex 요소를 세로선 상에서 정렬

```
flex-start , flex-end , center , baseline , stretch (default)
```



3. `flex-direction` - 정렬할 방향을 지정

```
row (default) , row-reverse , column , column-reverse
```



4. `order` - Flex 요소의 순서를 지정

```
<integer> (... -1, 0 (default), 1, ...)

e.g.

#pond {
  display: flex;
}

.red {
order: -2;
}
```



5. `align-self` - 지정된 `align-items` 값을 무시하고 Flex 요소를 세로선 상에서 정렬

```
flex-start , flex-end , center , baseline , stretch
```



6. `flex-wrap` - Flex 요소들을 한 줄 또는 여러 줄에 걸쳐 정렬

```
nowrap (default) , wrap , wrap-reverse
```



7. `flex-flow` - 다음의 속성들을 간략히 한 속성 : `flex-direction` and `flex-wrap`.

```
<flex-direction> , <flex-wrap>
```



8. `align-content` - 세로선 상에 여분의 공간이 있는 경우 Flex 컨테이너 사이의 간격을 조절

```
flex-start , flex-end , center , space-between , space-around , space-evenly ,  stretch (default)
```

