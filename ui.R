library(shiny)

shinyUI(fluidPage(
   titlePanel("How does infection spread?"),
   
   sidebarLayout(
      sidebarPanel(
         helpText("See the spread of infection to different users."),
      
      selectInput("user", 
        label = "Choose a user to infect:",
        choices = list("A", "B", "C", "D", "E", "F", 
                       "G", "H", "I", "J", "K", "L", 
                       "M", "N", "O", "P", "Q", "R", 
                       "S", "T", "U", "V", "W", "X", 
                       "Y", "Z"),
        selected = "A"),
      
      selectInput("color", 
                  label = "Choose a color for infected users:",
                  choices = list("blue",
                                 "green",
                                 "orange",
                                 "red",
                                 "purple"),
                  selected = "red")
      
    ),
    
    mainPanel(
      plotOutput("plot"),
      textOutput("text1")
    )
  )
))