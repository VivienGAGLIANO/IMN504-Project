#ifndef SCENE_H
#define SCENE_H

#include <vector>

#include "camera.h"
#include "engine.h"
#include "object.h"

struct Light{};
// struct Camera{};

class Engine;

class Scene
{
public:
	~Scene();
	void update(const double& delta_time);
	void render(Engine* engine);
	static Scene* get_instance();

private:
	Scene();

	static Scene *instance;
	// Light light;
	Camera camera;
	std::vector<Object*> objects;
};

#endif