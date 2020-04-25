#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>
#include <sstream>
#include <stdint.h>
#include <iostream>


void readVertex3D(const std::string &line, std::string &token, std::vector<float> &vertices)
{
    std::istringstream lineStream(line);
    std::getline(lineStream, token, ' ');

    std::getline(lineStream, token, ' ');
    vertices.push_back(std::stof(token));
    std::getline(lineStream, token, ' ');
    vertices.push_back(std::stof(token));
    std::getline(lineStream, token, ' ');
    vertices.push_back(std::stof(token));
}

void readVertex2D(const std::string &line, std::string &token, std::vector<float> &vertices)
{
    std::istringstream lineStream(line);
    std::getline(lineStream, token, ' ');

    std::getline(lineStream, token, ' ');
    vertices.push_back(std::stof(token));
    std::getline(lineStream, token, ' ');
    vertices.push_back(std::stof(token));
}


std::vector<float> readFlatVerticesFromString(const std::string &allLines)
{
    std::stringstream linesStream(allLines);

    std::vector<float> vertices;

    std::string tokenBuffer;

    for(std::string line; std::getline(linesStream, line); ){
        if(line.size() < 2)
            continue;
        if((line[0] == 'v') && (line[1] == ' '))
            readVertex3D(line, tokenBuffer, vertices);
    }

    return vertices;
}


PYBIND11_MODULE(obj_import_cpp, m) {
    m.def("read_flat_vertices", &readFlatVerticesFromString, "");

}
