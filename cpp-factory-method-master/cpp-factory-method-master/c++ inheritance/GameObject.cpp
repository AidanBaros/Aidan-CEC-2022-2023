#include"GameObject.h"
#include<SFML/Graphics.hpp>

void star::draw(sf::RenderWindow& window) { //passes a POINTER to the gamescreen
    sf::CircleShape triangle1(30, 3);
    triangle1.setFillColor(sf::Color(0, 200, 255));
    triangle1.setPosition(xpos, ypos);
    window.draw(triangle1);//draw to gamescreen

    sf::CircleShape triangle2(30, 3);
    triangle2.setFillColor(sf::Color(200, 200, 255));
    triangle2.setPosition(xpos + 40, ypos - 15);
    triangle2.rotate(60); //twist to make star shape
    window.draw(triangle2);
}

void duck::draw(sf::RenderWindow& window) {
    sf::CircleShape circle1(60);
    circle1.setFillColor(sf::Color(255, 255, 0));
    circle1.setPosition(xpos, ypos);
    window.draw(circle1);//draw to gamescreen

    sf::RectangleShape rect1(sf::Vector2f(120, 60));
    rect1.setFillColor(sf::Color(0, 0, 0));
    rect1.setPosition(xpos, ypos);
    window.draw(rect1);

    sf::CircleShape circle2(30);
    circle2.setFillColor(sf::Color(255, 255, 0));
    circle2.setPosition(xpos + 80, ypos+30);
    window.draw(circle2);

    sf::CircleShape circle3(5);
    circle3.setFillColor(sf::Color(0, 200, 255));
    circle3.setPosition(xpos + 110, ypos + 40);
    window.draw(circle3);//draw to gamescreen

    sf::CircleShape triangle1(15,3);
    triangle1.setFillColor(sf::Color(200, 200, 0));
    triangle1.setPosition(xpos + 5, ypos + 45);
    triangle1.rotate(50);
    window.draw(triangle1);//draw to gamescreen

    sf::CircleShape triangle2(30,3);
    triangle2.setFillColor(sf::Color(200, 200, 0));
    triangle2.setPosition(xpos + 50, ypos + 40);
    triangle2.rotate(45); //twist to make star shape
    window.draw(triangle2);

    sf::CircleShape triangle3(15,3);
    triangle3.setFillColor(sf::Color(255, 165, 0));
    triangle3.setPosition(xpos + 120, ypos + 55);
    triangle3.rotate(-30); //twist to make star shape
    window.draw(triangle3);
}