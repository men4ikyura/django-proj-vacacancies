async function getIds() {
    const url = "https://api.hh.ru/vacancies";
    const params = new URLSearchParams({
        order_by: 'publication_time',
        search_field: 'name',
        text: 'системный администратор',
        per_page: '10'
    });

    try {
        const response = await fetch(`${url}?${params}`);
        const data = await response.json();
        const listIds = data.items.map(item => item.id);
        return listIds;
    } catch (error) {
        console.error("Ошибка при получении ID вакансий:", error);
        return [];
    }
}


function formatData(data) {
    const description = data.description
        ? data.description.replace(/<[^>]+>/g, " ").replace(/&quot;/g, "")
        : "Нет информации";

    const keySkills = data.key_skills && data.key_skills.length
        ? formatFieldSkills(data.key_skills)
        : "Нет информации";

    const salary = formatSalary(data.salary);

    const publishedAt = data.published_at
        ? new Date(data.published_at).toLocaleString("ru-RU")
        : "Нет информации";

    return {
        name: data.name || "Нет информации",
        description,
        keySkills,
        employerName: data.employer?.name || "Нет информации",
        salary,
        city: data.area?.name || "Нет информации",
        publishedAt
    };
}


function formatSalary(salary) {
    if (!salary) return "Нет информации";
    const { from, to, currency } = salary;

    if (!from) return `${to} ${currency}`;
    if (!to) return `${from} ${currency}`;
    return `${Math.round((from + to) / 2)} ${currency}`;
}

function formatFieldSkills(skills) {
    return skills.map(skill => skill.name).join(", ");
}


async function infoIdsVac(listIds) {
    const container = document.getElementById('vacancies-container');
    for (const id of listIds) {
        try {
            const response = await fetch(`https://api.hh.ru/vacancies/${id}`);
            const data = await response.json();
            const formattedData = formatData(data);
            const vacancyElement = document.createElement('div');
            console.log(formattedData.description);
            console.log(formattedData.description.length);
            vacancyElement.classList.add('device');
            vacancyElement.innerHTML = `
                <h2 class="device-title">Название профессии: <strong>${formattedData.name}</strong></h2>
                <p class="device-description">
                    <strong>Описание:</strong>
                    <span class="short-description">
                    ${formattedData.description.length > 100 ? formattedData.description.slice(0, 100) : formattedData.description}
                    </span>
                    <span class="full-description" style="display: none;"> ${formattedData.description}</span>
                    <button class="toggle-description">Читать полностью</button>
                </p>
                <p class="device-skills"><strong>Навыки:</strong> ${formattedData.keySkills}</p>
                <p class="device-employer"><strong>Название компании:</strong> ${formattedData.employerName}</p>
                <p class="device-salary"><strong>Оклад:</strong> ${formattedData.salary}</p>
                <p class="device-area"><strong>Название региона:</strong> ${formattedData.city}</p>
                <p class="device-published"><strong>Дата публикации:</strong> ${formattedData.publishedAt}</p>
                 `;
            container.appendChild(vacancyElement);
        } catch (error) {
            console.error(`Ошибка при обработке вакансии ID ${id}:`, error);
        }
    }
}


async function updateParsedData() {
    const idLists = await getIds();
    if (idLists.length) {
        await infoIdsVac(idLists);
    } else {
        console.log("Нет данных для обработки.");
    }
}

updateParsedData();

